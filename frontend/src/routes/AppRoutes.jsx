import { Navigate, Route, Routes } from "react-router-dom";
import LandingPage from "../pages/LandingPage";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import DashboardPage from "../pages/DashboardPage";
import SwipePage from "../pages/SwipePage";
import ChatPage from "../pages/ChatPage";
import NotificationsPage from "../pages/NotificationsPage";
import AdminPage from "../pages/AdminPage";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="/swipe" element={<SwipePage />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/notifications" element={<NotificationsPage />} />
      <Route path="/admin" element={<AdminPage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
