<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';
import AppHeader from '@/components/AppHeader.vue';

const authStore = useAuthStore();

// Vérifier l'authentification au chargement de l'app
onMounted(() => {
  authStore.checkAuth();
});
</script>

<template>
  <div id="app">
    <AppHeader />
    
    <main class="main-content">
      <RouterView />
    </main>

    <footer class="app-footer">
      <p>&copy; 2025 Movie Platform - Tous droits réservés</p>
    </footer>
  </div>
</template>

<style>
/* Reset et styles globaux */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background-color: #f5f5f5;
  color: #333;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
}

.app-footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}
</style>