import { useEffect, useMemo, useState } from "react";
import { api } from "../api/client";
import { createWs } from "../websocket/client";

export default function ChatPage() {
  const [roomId, setRoomId] = useState("");
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState("");
  const socket = useMemo(() => (roomId ? createWs(`chat/${roomId}/`) : null), [roomId]);

  useEffect(() => {
    if (!roomId) return;
    api.get(`/chat/messages/?room=${roomId}`).then((res) => setMessages(res.data.results || []));
  }, [roomId]);

  useEffect(() => {
    if (!socket) return;
    socket.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      if (payload.event_type === "typing") return;
      setMessages((prev) => [...prev, { content: payload.message, sender: payload.sender }]);
    };
    return () => socket.close();
  }, [socket]);

  const send = async () => {
    if (!text.trim() || !roomId) return;
    await api.post("/chat/messages/", { room: roomId, content: text, message_type: "text" });
    socket?.send(JSON.stringify({ type: "message", message: text }));
    setText("");
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-3xl rounded-2xl border border-white/10 bg-white/5 p-6">
        <h2 className="text-2xl font-semibold">Real-time Chat</h2>
        <input className="mt-3 w-full rounded bg-slate-900 p-2" placeholder="Room UUID" value={roomId} onChange={(e) => setRoomId(e.target.value)} />
        <div className="mt-4 h-80 overflow-y-auto rounded bg-slate-900 p-3">
          {messages.map((m, i) => <p key={i} className="mb-2"><span className="text-pink-300">{m.sender || "you"}:</span> {m.content}</p>)}
        </div>
        <div className="mt-3 flex gap-2">
          <input
            className="flex-1 rounded bg-slate-900 p-2"
            value={text}
            onChange={(e) => {
              setText(e.target.value);
              socket?.send(JSON.stringify({ type: "typing" }));
            }}
            placeholder="Type message"
          />
          <button onClick={send} className="rounded bg-pink-500 px-4">Send</button>
        </div>
      </div>
    </div>
  );
}
