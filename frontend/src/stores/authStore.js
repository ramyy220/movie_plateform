import { defineStore } from 'pinia';
import authService from '@/services/authService';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('token') || null,
    isAuthenticated: !!localStorage.getItem('token'),
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

    async login (credentials) {
      this.loading = true;
      this.error = null;

      try {
        const response = await authService.login(credentials)
        this.user = response.user
        this.token = response.token
        this.isAuthenticated = true
        
        localStorage.setItem('token', response.token)
        localStorage.setItem('user', JSON.stringify(response.user))
        
        return response
      } catch (error) {
        this.error = error.message || 'Login failed';
        throw error;
      } finally {
        this.loading = false;
      }
    },
    
    logout () {
      this.loading = true;
      this.error = null;
      try {
        this.user = null
        this.token = null
        this.isAuthenticated = false
        
        localStorage.removeItem('token')
        localStorage.removeItem('user')
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
      if (authService.isAuthenticated()) {
        try {
          const user = await authService.getCurrentUser();
          this.user = user;
          this.isAuthenticated = true;
        } catch (error) {
          await this.logout();
        }
      }
    }
  }
});