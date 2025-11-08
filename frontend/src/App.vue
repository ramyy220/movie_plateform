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
<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  padding: 1rem;
  flex: 1;
}

.app-footer {
  text-align: center;
  padding: 1rem 0;
  border-top: 1px solid rgba(255, 255, 255, 0.03);
  margin-top: auto; 
  color: #aaa;
  font-size: 0.9rem;
}
</style>