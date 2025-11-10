<template>
  <header class="app-header">
    <div class="container" @click="handlehome">
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
const handlehome = () => {
  router.push('/');
};
</script>

<style scoped>
.app-header{
  position:sticky;
  top:0;
  z-index:60;
  padding:0.6rem 0;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent 60%);
  backdrop-filter: blur(8px);
  border-bottom:1px solid rgba(255,255,255,0.03);
}

.container{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:1rem;
}

/* Logo */
.logo{
  display:inline-flex;
  align-items:center;
  gap:0.6rem;
  font-weight:700;
  font-size:1.05rem;
  color: #fff;
  padding:0.25rem 0.5rem;
  border-radius:8px;
}

/* Nav on the right */
nav{
  display:flex;
  align-items:center;
  gap:0.75rem;
}

/* Welcome text */
.welcome{
  color:var(--muted);
  font-weight:600;
  margin-right:0.5rem;
  font-size:0.95rem;
}

/* Links in header */
.btn-link{
  padding:0.45rem 0.7rem;
  border-radius:999px;
  color:var(--muted);
  background:transparent;
  border:1px solid transparent;
  transition: color .12s, transform .12s;
}
.btn-link:hover{ color:#fff; transform:translateY(-2px) }

/* Logout button */
.btn-logout{
  background: #534a61;
  border:none;
  color:#fff;
  padding:0.45rem 0.75rem;
  border-radius:999px;
  font-weight:700;
  cursor:pointer;
  box-shadow: 0 8px 24px rgba(124,92,255,0.12);
}
.btn-logout:hover{ transform:translateY(-3px) }

/* Small screens: compact header */
@media (max-width:520px){
  .welcome{ display:none }
  .logo{ font-size:0.98rem }
  nav{ gap:0.5rem }
}
</style>

