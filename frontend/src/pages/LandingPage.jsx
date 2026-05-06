import { Link } from "react-router-dom";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-4xl rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur">
        <h1 className="text-4xl font-bold">SparkUp</h1>
        <p className="mt-3 text-slate-300">Swipe, match, chat, communities, and events in one social app.</p>
        <div className="mt-6 flex gap-3">
          <Link to="/register" className="rounded-lg bg-pink-500 px-4 py-2">Create account</Link>
          <Link to="/login" className="rounded-lg border border-white/20 px-4 py-2">Login</Link>
        </div>
      </div>
    </div>
  );
}
