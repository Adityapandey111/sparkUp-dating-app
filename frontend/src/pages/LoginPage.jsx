import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { api } from "../api/client";
import { setAuth } from "../redux/store";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const onSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await api.post("/auth/login/", { email, password });
      dispatch(setAuth({ access: data.access, refresh: data.refresh }));
      navigate("/dashboard");
    } catch {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="min-h-screen grid place-items-center bg-slate-950 text-slate-100">
      <form onSubmit={onSubmit} className="w-full max-w-md rounded-2xl border border-white/10 bg-white/5 p-6 space-y-3">
        <h2 className="text-2xl font-semibold">Login</h2>
        {error && <p className="text-red-400 text-sm">{error}</p>}
        <input className="w-full rounded bg-slate-900 p-2" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" className="w-full rounded bg-slate-900 p-2" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button className="w-full rounded bg-pink-500 p-2">Login</button>
        <p className="text-sm">No account? <Link className="text-pink-300" to="/register">Register</Link></p>
      </form>
    </div>
  );
}
