<template>
  <header class="app-header">
    <div class="container">
      <router-link to="/" class="logo">
        🎬 Movie Platform
      </router-link>
      
      <nav>
        <template v-if="authStore.isLoggedIn">
          <span class="welcome">Salut, {{ authStore.currentUser?.username }} !</span>
          <button @click="handleLogout" class="btn-logout">Déconnexion</button>
        </template>
        <template v-else>
          <router-link to="/login" class="btn-link">Connexion</router-link>
          <router-link to="/register" class="btn-link">Inscription</router-link>
        </template>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const handleLogout = async () => {
  await authStore.logout();
  router.push('/login');
};
</script>

<style scoped>
.app-header {
  background-color: #333;
  color: white;
  padding: 1rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.welcome {
  color: #4CAF50;
}

.btn-link, .btn-logout {
  padding: 0.5rem 1rem;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn-link {
  background-color: #4CAF50;
}

.btn-link:hover {
  background-color: #45a049;
}

.btn-logout {
  background-color: #f44336;
  border: none;
  cursor: pointer;
}

.btn-logout:hover {
  background-color: #da190b;
}
</style>