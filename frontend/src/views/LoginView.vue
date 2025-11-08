<template>
     <div class="auth.container">
        <div class="auth-card">
            <h1> Connectez-vous à Movie plateforme 🎬</h1>
            <form @submit.prevent="handleLogin">
                <div class="form-group">
                    <label for="email">E-mail</label>
                    <input 
                     type="email"
                     id="email"
                     v-model="form.email"
                        required
                        placeholder="Entrez votre e-mail" />
                </div>
                <div class="form-group">
                    <label for="password"> Mot de passe </label>
                    <input 
                        type="password"
                        id="password"
                        v-model="form.password"
                            required
                            placeholder="Entrez votre mot de passe" />
                </div>
                <div v-if="error" class="error-message">
                    {{ error }}
                </div>
                <button type="submit" :disabled="loading" class="btn-primary">
                    {{ loading ? 'Connexion...' : 'Se connecter' }}
                </button>
            </form>
            <div class="auth-footer">
                <p>Vous n'avez pas de compte ? <router-link to="/register">Inscrivez-vous</router-link></p>
            </div>
        </div>
     </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';

const authService = useAuthStore();
const router = useRouter();

const form = ref({
    email: '',
    password: ''
});
const loading = ref(false);
const error = ref(null);

const handleLogin = async () => {
    loading.value = true;
    error.value = null;
    try {
        await authService.login(form.value.email, form.value.password);
        router.push('/');
    } catch (err) {
        error.value = 'Échec de la connexion. Veuillez vérifier vos informations.';
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