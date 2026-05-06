import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function SwipePage() {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    api.get("/profiles/").then((res) => setProfiles(res.data.results || []));
  }, []);

  const swipe = async (targetId, swipeType) => {
    await api.post("/swipes/", { target: targetId, swipe_type: swipeType });
    setProfiles((prev) => prev.filter((p) => p.user !== targetId));
  };

  const current = profiles[0];
  return (
    <div className="min-h-screen grid place-items-center bg-slate-950 text-slate-100 p-6">
      {current ? (
        <div className="w-full max-w-md rounded-2xl border border-white/10 bg-white/5 p-6">
          <h2 className="text-xl font-semibold">User {current.user}</h2>
          <p className="text-slate-300 mt-2">{current.bio}</p>
          <div className="mt-6 flex gap-3">
            <button onClick={() => swipe(current.user, "pass")} className="flex-1 rounded bg-slate-700 p-2">Pass</button>
            <button onClick={() => swipe(current.user, "like")} className="flex-1 rounded bg-pink-500 p-2">Like</button>
            <button onClick={() => swipe(current.user, "super")} className="flex-1 rounded bg-purple-500 p-2">Super</button>
          </div>
        </div>
      ) : (
        <p>No profiles right now.</p>
      )}
    </div>
  );
}
