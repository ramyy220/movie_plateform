<template>
  <main class="main-content">
    <div class="container">
      <div class="account-card card">
        <h1>Mon compte</h1>

        <form @submit.prevent="onSubmit" class="account-form">
          <div class="form-group">
            <label>Nom d'utilisateur</label>
            <input v-model="username" type="text" required placeholder="Votre nom d'utilisateur" />
          </div>

          <div class="form-group">
            <label>Mot de passe actuel</label>
            <div class="pwd-row">
              <input :type="showCurrent ? 'text' : 'password'" v-model="currentPassword" required placeholder="Mot de passe actuel" />
              <button type="button" @click="showCurrent = !showCurrent" class="btn-ghost small-toggle">
                {{ showCurrent ? 'Masquer' : 'Afficher' }}
              </button>
            </div>
          </div>

          <div class="form-group">
            <label>Nouveau mot de passe (laisser vide si inchangé)</label>
            <div class="pwd-row">
              <input :type="showNew ? 'text' : 'password'" v-model="newPassword" placeholder="Nouveau mot de passe" />
              <button type="button" @click="showNew = !showNew" class="btn-ghost small-toggle">
                {{ showNew ? 'Masquer' : 'Afficher' }}
              </button>
            </div>
          </div>

          <div class="form-group">
            <label>Confirmer nouveau mot de passe</label>
            <input :type="showNew ? 'text' : 'password'" v-model="confirmPassword" placeholder="Confirmer le nouveau mot de passe" />
          </div>

          <div class="actions">
            <button type="submit" :disabled="loading" class="btn-primary">
              {{ loading ? 'Enregistrement...' : 'Enregistrer' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import authService from '../services/authService'

const username = ref('')
const currentPassword = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const showCurrent = ref(false)
const showNew = ref(false)
const loading = ref(false)

onMounted(async () => {
  try {
    const user = await authService.getCurrentUser()
    username.value = user?.username || ''
  } catch (e) {
    console.warn('Impossible de récupérer l\'utilisateur', e)
  }
})

async function verifyCurrentPassword() {
  const res = await axios.post('http://localhost:5000/auth/verify-password', { password: currentPassword.value })
  return res.status === 200
}

async function onSubmit() {
  if (!currentPassword.value) {
    alert('Veuillez saisir votre mot de passe actuel pour valider les changements.')
    return
  }

  if (newPassword.value) {
    if (newPassword.value !== confirmPassword.value) {
      alert('Les nouveaux mots de passe ne correspondent pas.')
      return
    }
    if (newPassword.value.length < 8) {
      alert('Le nouveau mot de passe doit contenir au moins 8 caractères.')
      return
    }
  }

  loading.value = true
  try {
    const ok = await verifyCurrentPassword()
    if (!ok) {
      alert('Mot de passe actuel incorrect.')
      return
    }

    const payload = { username: username.value }
    if (newPassword.value) payload.password = newPassword.value

    await axios.post('http://localhost:5000/user/update', payload)
    alert('Profil mis à jour avec succès.')
    currentPassword.value = ''
    newPassword.value = ''
    confirmPassword.value = ''
    const stored = authService.getUser()
    if (stored) {
      stored.username = username.value
      localStorage.setItem('user', JSON.stringify(stored))
    }
  } catch (err) {
    console.error(err)
    alert(err?.response?.data?.message || 'Erreur lors de la mise à jour du compte.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.account-card {
  width: 100%;
  max-width: 520px;
  margin: 12px auto;
  padding: 28px;
  border-radius: 12px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border: 1px solid rgba(255,255,255,0.04);
  box-shadow: 0 12px 36px rgba(2,6,23,0.6);
  color: #eaf3ff;
  backdrop-filter: blur(6px);
}

.account-card h1{
  margin: 0 0 18px;
  text-align: left;
  color: #fff;
  font-weight:700;
  font-size:1.05rem;
}

/* Reuse form-group look from LoginView for consistency */
.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display:block;
  margin-bottom:8px;
  font-weight:600;
  color: var(--muted);
  font-size: 0.95rem;
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
  color: rgba(234,243,255,0.45);
}

.form-group input:focus {
  outline:none;
  border-color: var(--accent-2);
  box-shadow: 0 6px 24px rgba(124,92,255,0.08);
}

/* Password row & toggle */
.pwd-row {
  display:flex;
  gap:10px;
  align-items:center;
}

.pwd-row input { flex:1; }

/* small toggle button (uses ghost style) */
.small-toggle {
  padding:8px 10px;
  border-radius:8px;
  font-weight:600;
  color: var(--muted);
  background: transparent;
  border: 1px solid rgba(255,255,255,0.04);
  cursor: pointer;
}

/* reuse primary button look */
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

/* actions spacing */
.actions { margin-top: 12px; }
</style>
