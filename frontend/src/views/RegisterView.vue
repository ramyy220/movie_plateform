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
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 20px;
}

.auth-card {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.auth-card h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #555;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #4CAF50;
}

.btn-primary {
  width: 100%;
  padding: 14px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover:not(:disabled) {
  background-color: #45a049;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  background-color: #fee;
  color: #c33;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 20px;
  text-align: center;
}

.auth-footer {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.auth-footer a {
  color: #4CAF50;
  text-decoration: none;
  font-weight: 600;
}

.auth-footer a:hover {
  text-decoration: underline;
}
</style>