import { useEffect, useState } from "react";
import { api } from "../api/client";

export default function AdminPage() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get("/admin/stats/").then((res) => setStats(res.data));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-3xl rounded-2xl border border-white/10 bg-white/5 p-6">
        <h2 className="text-2xl font-semibold">Admin Stats</h2>
        {stats ? (
          <div className="mt-4 grid grid-cols-2 gap-3">
            {Object.entries(stats).map(([k, v]) => (
              <div key={k} className="rounded bg-slate-900 p-3">
                <p className="text-slate-400 text-sm">{k}</p>
                <p className="text-2xl font-semibold">{v}</p>
              </div>
            ))}
          </div>
        ) : (
          <p className="mt-3">Loading...</p>
        )}
      </div>
    </div>
  );
}
