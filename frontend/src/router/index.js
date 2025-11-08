import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: { guest: true }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
      meta: { guest: true }
    },
  ],
});

// Quard de navigation pour proteger les routes 
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  
  // Si la route nécessite une authentification
  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    next('/login');
  }
  // Si l'utilisateur est connecté et essaie d'accéder à login/register
  else if (to.meta.guest && authStore.isLoggedIn) {
    next('/');
  }
  else {
    next();
  }
});

export default router
