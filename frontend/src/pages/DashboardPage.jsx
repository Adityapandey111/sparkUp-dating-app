import { Link } from "react-router-dom";

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-5xl rounded-2xl border border-white/10 bg-white/5 p-6">
        <h2 className="text-2xl font-semibold">Dashboard</h2>
        <div className="mt-4 grid grid-cols-2 gap-3 md:grid-cols-4">
          <Link className="rounded bg-slate-900 p-3" to="/swipe">Swipe</Link>
          <Link className="rounded bg-slate-900 p-3" to="/chat">Chat</Link>
          <Link className="rounded bg-slate-900 p-3" to="/notifications">Notifications</Link>
          <Link className="rounded bg-slate-900 p-3" to="/admin">Admin</Link>
        </div>
      </div>
    </div>
  );
}
