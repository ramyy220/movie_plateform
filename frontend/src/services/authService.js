import axios from 'axios';

const API_URL = 'http://localhost:5000/auth';

axios.defaults.withCredentials = false;

axios.interceptors.request.use(
    (config) => {
        // s'assurer que headers existe
        config.headers = config.headers || {};
        const token = localStorage.getItem('access_token');
        if (token && token !== 'null') {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        config.headers['Content-Type'] = 'application/json';
        return config;
    },
    (error) => Promise.reject(error)
);

export default {
    async register(username, email, password) {
        const response = await axios.post(`${API_URL}/register`, { username, email, password });
        if (response.data.access_token) {
            localStorage.setItem('access_token', response.data.access_token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
        }
        return response.data;
    },

    async login(email, password) {
        const response = await axios.post(`${API_URL}/login`, { email, password });
        if (response.data.access_token) {
            localStorage.setItem('access_token', response.data.access_token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
        }
        return response.data;
    },

    async logout(){
        try {
            await axios.post(`${API_URL}/logout`, {});
        } catch (error) {
            console.error('Error logging out user:', error);
        } finally {
            localStorage.removeItem('access_token');
            localStorage.removeItem('user');
        }
    },

    async getCurrentUser() {
        const response = await axios.get(`${API_URL}/me`);
        return response.data.user;
    },

    isAuthenticated() {
        return !!localStorage.getItem('access_token');
    },

    getToken() {
        return localStorage.getItem('access_token');
    },

    getUser() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    },
};