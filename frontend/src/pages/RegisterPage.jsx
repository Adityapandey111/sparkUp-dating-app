import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api/client";

export default function RegisterPage() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const onSubmit = async (e) => {
    e.preventDefault();
    await api.post("/auth/register/", form);
    setMessage("Registration successful. Check your email for verification.");
    setTimeout(() => navigate("/login"), 1200);
  };

  return (
    <div className="min-h-screen grid place-items-center bg-slate-950 text-slate-100">
      <form onSubmit={onSubmit} className="w-full max-w-md rounded-2xl border border-white/10 bg-white/5 p-6 space-y-3">
        <h2 className="text-2xl font-semibold">Register</h2>
        {message && <p className="text-emerald-300 text-sm">{message}</p>}
        <input className="w-full rounded bg-slate-900 p-2" placeholder="Username" value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} />
        <input className="w-full rounded bg-slate-900 p-2" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input type="password" className="w-full rounded bg-slate-900 p-2" placeholder="Password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <button className="w-full rounded bg-pink-500 p-2">Create account</button>
      </form>
    </div>
  );
}
