import authService from "./authService";

const API_BASE = window.__BACKEND_URL__ || import.meta.env.VITE_API_BASE || "http://localhost:5000";

function authHeaders() {
    const token = authService.getToken();
    return token ? { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' } : { 'Content-Type': 'application/json' };
}

export async function getFavorites() {
  const res = await fetch(`${API_BASE}/favorites`, { headers: authHeaders() });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

export async function addFavorite(movie) {
    const re = await fetch(`${API_BASE}/favorites`, {
        method: 'POST',
        headers: authHeaders(),
        body: JSON.stringify(movie)
    });
    if (!re.ok) throw new Error(`HTTP ${re.status}`);
    return re.json();
}

export async function removeFavorite(movieId) {
    const re = await fetch(`${API_BASE}/favorites/${movieId}`, {
        method: 'DELETE',
        headers: authHeaders()
    });
    if (!re.ok) throw new Error(`HTTP ${re.status}`);
    return re.json();
}

