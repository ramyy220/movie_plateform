import { defineStore } from 'pinia';
import authService from '@/services/authService';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: authService.getUser(),
        isAuthenticated: authService.isAuthenticated(),
        loading : false,
        error: null,
    }),
    
    getters: {
        currentUser : (state) => state.user,
        isLoggedIn : (state) => state.isAuthenticated,
    },

    actions: {
        async register (username, email, password) {
            this.loading = true;
            this.error = null;

            try {
                const data = await authService.register(username, email, password);
                this.user = data.user;
                this.isAuthenticated = true;
                return data;
            } catch (error) {
                this.error = error.message || 'Registration failed';
                throw error;
            } finally {
                this.loading = false;
            }
        },

        async login (email, password) {
            this.loading = true;
            this.error = null;

            try {
                const data = await authService.login(email, password);
                this.user = data.user;
                this.isAuthenticated = true;
                return data;
            } catch (error) {
                this.error = error.message || 'Login failed';
                throw error;
            } finally {
                this.loading = false;
            }
        },
        
        async logout () {
            this.loading = true;
            this.error = null;
            try {
                await authService.logout();
                this.user = null;
                this.isAuthenticated = false;
            }
            catch (error) {
                this.error = error.message || 'Logout failed';
                throw error;
            }
            finally {
                this.loading = false;
            }
        },

        async checkAuth() {
            this.loading = true;
            this.error = null;

            if (!authService.isAuthenticated()) {
                this.loading = false;
                return;
            }

            try {
                const user = await authService.getCurrentUser();
                this.user = user;
                this.isAuthenticated = true;
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('user');
                    this.user = null;
                    this.isAuthenticated = false;
                } else {
                    console.error('checkAuth error:', error);
                }
            } finally {
                this.loading = false;
            }
        }
    }
});