import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function NotificationsPage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    api.get("/notifications/").then((res) => setItems(res.data.results || []));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-3xl rounded-2xl border border-white/10 bg-white/5 p-6">
        <h2 className="text-2xl font-semibold">Notifications</h2>
        <div className="mt-4 space-y-2">
          {items.map((n) => <div key={n.id} className="rounded bg-slate-900 p-3">{n.message}</div>)}
        </div>
      </div>
    </div>
  );
}
