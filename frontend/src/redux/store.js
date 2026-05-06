import { configureStore, createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
  name: "auth",
  initialState: {
    access: localStorage.getItem("sparkup_access"),
    refresh: localStorage.getItem("sparkup_refresh"),
    user: null,
  },
  reducers: {
    setAuth: (state, action) => {
      state.access = action.payload.access;
      state.refresh = action.payload.refresh;
      localStorage.setItem("sparkup_access", action.payload.access);
      localStorage.setItem("sparkup_refresh", action.payload.refresh);
    },
    clearAuth: (state) => {
      state.access = null;
      state.refresh = null;
      state.user = null;
      localStorage.removeItem("sparkup_access");
      localStorage.removeItem("sparkup_refresh");
    },
  },
});

export const { setAuth, clearAuth } = authSlice.actions;

export const store = configureStore({
  reducer: { auth: authSlice.reducer },
});
