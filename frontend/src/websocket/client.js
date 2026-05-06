export function createWs(path) {
  const base = import.meta.env.VITE_WS_URL || "ws://localhost:8000/ws";
  return new WebSocket(`${base}/${path}`);
}
