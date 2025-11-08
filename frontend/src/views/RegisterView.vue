<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1>🎬 Inscription à Movie Plateforme</h1>
      
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">Nom d'utilisateur</label>
          <input
            type="text"
            id="username"
            v-model="form.username"
            required
            placeholder="votre_pseudo"
          />
        </div>

        <div class="form-group">
          <label for="email">E-mail</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            required
            placeholder="votre@email.com"
          />
        </div>

        <div class="form-group">
          <label for="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            required
            placeholder="••••••••"
            minlength="6"
          />
        </div>

        <div class="form-group">
          <label for="confirmPassword">Confirmer le mot de passe</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="form.confirmPassword"
            required
            placeholder="••••••••"
          />
        </div>

        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <button type="submit" :disabled="loading" class="btn-primary">
          {{ loading ? 'Inscription...' : "S'inscrire" }}
        </button>
      </form>

      <div class="auth-footer">
        <p>Déjà un compte ? <router-link to="/login">Se connecter</router-link></p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const authStore = useAuthStore();

const form = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: ''
});

const loading = ref(false);
const error = ref(null);

const handleRegister = async () => {
  // Validation des mots de passe
  if (form.value.password !== form.value.confirmPassword) {
    error.value = 'Les mots de passe ne correspondent pas';
    return;
  }

  if (form.value.password.length < 6) {
    error.value = 'Le mot de passe doit contenir au moins 6 caractères';
    return;
  }

  loading.value = true;
  error.value = null;

  try {
    await authStore.register(
      form.value.username,
      form.value.email,
      form.value.password
    );
    router.push('/'); // Rediriger vers la page d'accueil
  } catch (err) {
    error.value = err.message || "Erreur lors de l'inscription";
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* dark / glassy auth styles — consistent with global theme */
.auth-container{
  display:flex;
  justify-content:center;
  align-items:center;
  min-height: calc(100vh - 120px);
  padding: 20px;
}

.auth-card{
  width:100%;
  max-width:420px;
  padding:32px;
  border-radius:12px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border: 1px solid rgba(255,255,255,0.04);
  box-shadow: 0 12px 36px rgba(2,6,23,0.6);
  color: #eaf3ff;
  backdrop-filter: blur(6px);
}

.auth-card h1{
  margin:0 0 18px;
  text-align:center;
  color: #fff;
  font-weight:700;
  font-size:1.05rem;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display:block;
  margin-bottom:8px;
  font-weight:600;
  color: var(--muted);
}

.form-group input {
  width:100%;
  padding:12px 14px;
  border-radius:10px;
  border:1px solid rgba(255,255,255,0.04);
  background: rgba(0,0,0,0.25);
  color: #eaf3ff;
  font-size:15px;
  transition: box-shadow .14s, border-color .14s;
}

.form-group input::placeholder {
  color: rgba(230,238,248,0.35);
}

.form-group input:focus {
  outline:none;
  border-color: var(--accent-2);
  box-shadow: 0 6px 24px rgba(124,92,255,0.08);
}

.btn-primary {
  width:100%;
  padding:12px 14px;
  border-radius:999px;
  background: #534a61;
  border:none;
  color:#fff;
  font-weight:700;
  font-size:15px;
  cursor:pointer;
  box-shadow: 0 10px 30px rgba(124,92,255,0.12);
  transition: transform .12s, opacity .12s;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-3px);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  background: rgba(255,90,90,0.08);
  color: #ffb3b3;
  padding:10px;
  border-radius:8px;
  margin-bottom:12px;
  text-align:center;
  border: 1px solid rgba(255,90,90,0.06);
}

.auth-footer {
  text-align: center;
  margin-top: 20px;
  color: var(--muted);
}

.auth-footer a {
  color: #534a61;
  text-decoration:none;
  font-weight:700;
}

.auth-footer a:hover {
  text-decoration: underline;
}

/* small screens */
@media (max-width:460px){
  .auth-card { padding: 20px; border-radius: 10px; }
  .auth-card h1 { font-size: 1rem; }
}
</style>