<template>
    <div class="container">
        <h1> Mes Favoris </h1>
        <div v-if="loading">Chargement...</div>
        <div v-if="error" class="error">{{ error }}</div>

        <div v-if="movies.length === 0  && !loading">Vous n'avez pas encore ajouté de films à vos favoris.</div>

        <div class="results" v-if="movies.length">
      <div v-for="m in movies" :key="m.movie_id" class="movie-card">
        <img v-if="m.poster_path" :src="'https://image.tmdb.org/t/p/w300'+m.poster_path" class="poster" />
        <div class="meta">
          <h3 class="title">{{ m.title }}</h3>
          <div class="info">
            <button class="btn-ghost" @click="remove(m.movie_id)">Retirer</button>
          </div>
        </div>
      </div>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getFavorites, removeFavorite } from '@/services/favService';

const movies = ref([]);
const loading = ref(false);
const error = ref(null);

async function load() {
    loading.value = true;
    error.value = null;
    try {
        const data = await getFavorites()
        movies.value = data;
    } catch (err) {
        error.value = 'Erreur lors du chargement des favoris.';
    } finally {
        loading.value = false;
    }
}

async function remove(movieId) {
    try {
        await removeFavorite(movieId);
        movies.value = movies.value.filter(m => m.movie_id !== movieId);
    } catch (err) {
        error.value = 'Erreur lors de la suppression du favori.';
    }
}

onMounted(() => {
    load();
});
</script>

<style scoped>
:root {
  --bg: #0f1724;
  --card: #0b1220;
  --muted: #9aa6b2;
  --accent: #ff6b6b;
  --glass: rgba(255,255,255,0.03);
  --radius: 10px;
  --shadow: 0 6px 18px rgba(2,6,23,0.6);
}

.container {
  max-width: 1100px;
  margin: 28px auto;
  padding: 24px;
  color: #e6eef6;
  background: linear-gradient(180deg, rgba(255,255,255,0.01), transparent);
  border-radius: 12px;
  min-height: 60vh;
}

/* Header */
.container h1 {
  margin: 0 0 16px 0;
  font-size: 1.6rem;
  letter-spacing: 0.2px;
  color: #fff;
}

/* Loading / Error */
.error {
  background: rgba(255,80,80,0.06);
  color: #ffb3b3;
  border-left: 4px solid rgba(255,80,80,0.28);
  padding: 10px 14px;
  margin-bottom: 12px;
  border-radius: 6px;
  font-size: 0.95rem;
}

.results {
  display: grid;
  /* augmenter la taille minimale des colonnes pour des cards plus larges */
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 18px;
  margin-top: 14px;
}

/* Movie card */
.movie-card {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  background: linear-gradient(180deg, var(--glass), rgba(255,255,255,0.01));
  padding: 16px; /* un peu plus d'espace */
  border-radius: calc(var(--radius) + 2px);
  box-shadow: var(--shadow);
  transition: transform 160ms ease, box-shadow 160ms ease;
  border: 1px solid rgba(255,255,255,0.02);
}

/* Poster */
.poster {
  width: 110px; /* plus large */
  height: 165px; /* plus haut */
  object-fit: cover;
  border-radius: 6px;
  flex-shrink: 0;
  background: linear-gradient(180deg,#0b1220,#091018);
  border: 1px solid rgba(255,255,255,0.03);
}

/* Title — permettre le wrapping pour voir tout le titre */
.title {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  color: #f7fbff;
  line-height: 1.25;
  white-space: normal;     /* autoriser le retour à la ligne */
  overflow: visible;       /* ne pas masquer */
  text-overflow: clip;
  word-break: break-word;  /* casser si trop long */
}

/* Info row */
.info {
  margin-top: 10px;
  display: flex;
  gap: 8px;
  align-items: center;
}

/* Buttons */
.btn-ghost {
  background: transparent;
  color: var(--accent);
  border: 1px solid rgba(255,107,107,0.16);
  padding: 6px 10px;
  border-radius: 8px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 140ms ease, transform 120ms ease;
}

.btn-ghost:hover {
  background: rgba(255,107,107,0.06);
  transform: translateY(-2px);
}

.container .empty {
  padding: 28px;
  text-align: center;
  color: var(--muted);
  font-size: 1rem;
}

/* Responsive tweaks */
@media (max-width: 520px) {
  .poster {
    width: 88px;
    height: 132px;
  }

  .container {
    padding: 16px;
  }

  .title {
    font-size: 0.98rem;
  }

  .results {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}
</style>