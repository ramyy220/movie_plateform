import axios from 'axios';

const API_URL = 'http://localhost:5000/auth';

//conf axios pour inclure le token jwt dans les requetes
axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
)

export default {
    async register(username, email, password) {
        try {
            const response = await axios.post(`${API_URL}/register`, {
                username,
                email,
                password
            });
            if (response.data.access_token) {
                localStorage.setItem('access_token', response.data.access_token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
            }
            return response.data;
        } catch (error) {
            console.error('Error registering user:', error);
            throw error;
        }
    },

    async login(email, password) {
        try {
            const response = await axios.post(`${API_URL}/login`, {
                email,
                password
            });
            if (response.data.access_token) {
                localStorage.setItem('access_token', response.data.access_token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
            }
            return response.data;
        } catch (error) {
            console.error('Error logging in user:', error);
            throw error;
        }
    },

    async logout(){
        try{
            await axios.post(`${API_URL}/logout`);
        }
        catch(error){
            console.error('Error logging out user:', error);
        }
        localStorage.removeItem('access_token');
        localStorage.removeItem('user');
    },

    async getCurrentUser() {
        try {
            const response = await axios.get(`${API_URL}/me`);
            return response.data.user;
        }
        catch (error) {
            console.error('Error fetching current user:', error);
            throw error;
        }
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
