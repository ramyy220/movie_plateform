<template>
  <header class="app-header">
    <div class="container">
      <router-link to="/" class="logo">
        🎬 Movie Platform
      </router-link>
      
      <nav>
        <template v-if="authStore.isLoggedIn">
          <span class="welcome">Salut, {{ authStore.currentUser?.username }} !</span>
          <div class="user-menu" ref="menuref">
            <button class="user-btn" @click="toggleMenu" :aria-expanded="showMenu" aria-haspopup="true" title="Mon profile">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5z" fill="currentColor"/>
                <path d="M2 20c0-2.761 4.477-5 10-5s10 2.239 10 5v1H2v-1z" fill="currentColor" opacity="0.9"/>
              </svg>
            </button>
            <transition name="fade">
              <ul v-if="showMenu" class="dropdown-menu" role="menu" aria-label="Menu utilisateur">
                <li class="menu-item" role="menuitem" @click="goTo('/account')">Mon compte</li>
                <li class="menu-item" role="menuitem" @click="goTo('/favorites')">Mes favoris</li>
                <li class="menu-item" role="menuitem" @click="goTo('/reviews')">Mes évaluations</li>
              </ul>
            </transition>
          </div>
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
import { ref } from 'vue';

const router = useRouter();
const authStore = useAuthStore();

const showMenu = ref(false);
const menuref = ref(null);

const toggleMenu = () => {
  showMenu.value = !showMenu.value;
};

const goTo = path => {
  showMenu.value = false;
  router.push(path);
}

const handleLogout = async () => {
  await authStore.logout();
  router.push('/login');
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

/* User button */
.user-menu{ position:relative; display:inline-block; }
.user-btn{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  width:36px;
  height:36px;
  border-radius:999px;
  background: #534a61;
  border:1px solid transparent;
  color:#fff;
  cursor:pointer;
  transition: transform .12s, background .12s;
}
.user-btn:hover{ transform:translateY(-2px); color:#fff; background: rgba(255,255,255,0.05); }

/* Dropdown menu */
.dropdown-menu{
  position:absolute;
  right:0;
  top:calc(100% + 8px);
  min-width:180px;
  background: rgba(10,10,12,0.95);
  border-radius:10px;
  padding:0.4rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  list-style:none;
  margin:0;
  z-index:80;
  border:1px solid rgba(255,255,255,0.03);
}
.menu-item{
  padding:0.55rem 0.75rem;
  color:var(--muted);
  cursor:pointer;
  border-radius:8px;
  font-weight:600;
  font-size:0.95rem;
}
.menu-item:hover{ background: rgba(255,255,255,0.03); color:#fff; }

.menu-divider{ height:1px; margin:0.35rem 0; background: rgba(255,255,255,0.02); border-radius:2px; }

menu-item.logout{ color:#fff; background: linear-gradient(90deg,#6b5ef0,#8457ff); font-weight:700; text-align:center; }

/* Simple fade transition */
.fade-enter-active, .fade-leave-active { transition: opacity .12s ease, transform .12s ease; }
.fade-enter-from, .fade-leave-to { opacity:0; transform: translateY(-6px); }

/* Small screens: compact header */
@media (max-width:520px){
  .welcome{ display:none }
  .logo{ font-size:0.98rem }
  nav{ gap:0.5rem }
}
</style>

