<template>
    <div class="search-container">
        <div class="search-bar">
            <input class="search-input" v-model="query" placeholder="Rechercher un film" @keyup.enter="search" />
            <button class="btn-primary" @click="search">Rechercher</button>
        </div>

        <div v-if="searched">
          <button class="back" @click="handleback" ><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg></button>
        </div>
        <div class="results">
            <div v-for="movie in movies" :key="movie.id" class="movie-card">
                <img
                    v-if="movie.poster_path"
                    :src="'https://image.tmdb.org/t/p/w300'+movie.poster_path"
                    alt="Affiche du film"
                    class="poster"
                />
                <div class="meta">
                    <h3 class="title">{{ movie.title }}</h3>
                    <p class="overview">{{ movie.overview }}</p>
                    <div class="info">
                        <span class="rating">⭐ {{ movie.vote_average ?? '—' }}</span>
                        <span class="date">{{ movie.release_date ?? 'N/A' }} </span>
                        <span>
                          <FavoriteButton
                            :id="movie.id"
                            :favorite-ids="favoriteIds"
                            @toggle="toggleFavorite"
                          />
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { searchMovies } from '../services/searchService';
import FavoriteButton from './FavoriteButton.vue';

const query = ref('');
const movies = ref([]);
const searched = ref(false);
const favoriteIds = ref([]);

const handleback = () => {
    movies.value = [];
    query.value = '';
    searched.value = false; 
};

function toggleFavorite(id) {
  if (favoriteIds.value.includes(id)) {
    favoriteIds.value = favoriteIds.value.filter(favId => favId !== id)
  } else {
    favoriteIds.value.push(id)
  }
}

const search = async () => {
    if (!query.value) return;
    searched.value = true;
    try {
        movies.value = await searchMovies(query.value);
    } catch (error) {
        console.error(error);
    }
};
</script>

<style scoped>
.search-container {
  max-width: 1100px;
  margin: 24px auto;
  padding: 25px;
  box-sizing: border-box;
}

.search-bar {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 18px;
}

.search-input {
  flex: 1;
  padding: 15px 25px;
  border-radius: 15px;
  border: 1px solid rgba(255,255,255,0.06);
  background: rgba(0,0,0,0.28);
  color: #eaf3ff;
  font-size: 18px;
  transition: box-shadow .12s, border-color .12s, transform .08s;
}

.search-input::placeholder {
  color: rgba(234,243,255,0.45);
}

.search-input:focus {
  outline: none;
  border-color: rgba(124,92,255,0.9);
  box-shadow: 0 8px 30px rgba(124,92,255,0.06);
  transform: translateY(-1px);
}

/* Button */
.btn-primary {
  padding: 11px 16px;
  border-radius: 15px;
  background: linear-gradient(180deg, #5a47b7, #4a3c92);
  border: none;
  color: #fff;
  font-weight: 900;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 10px 30px rgba(79,64,154,0.18);
  transition: transform .12s, opacity .12s;
  white-space: nowrap;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-3px);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.results {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 18px;
}

.movie-card {
  display: flex;
  gap: 15px;
  padding: 24px;
  border-radius: 12px;
  background: #2a293a;
  border: 1px solid rgba(255,255,255,0.03);
  box-shadow: 0 8px 28px rgba(2,6,23,0.45);
  color: #eaf3ff;
  min-height: 160px;
  overflow: hidden;
}

.poster {
  width: 120px;
  height: 180px;
  object-fit: cover;
  border-radius: 8px;
  flex-shrink: 0;
  box-shadow: 0 8px 20px rgba(0,0,0,0.45);
}

.meta {
  display: flex;
  flex-direction: column;
  gap: 12px;
  overflow: hidden;
}

.title {
  margin: 0;
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.15;
  white-space: normal;
  text-overflow: ellipsis;
  overflow: hidden;
}

.overview {
  margin: 0;
  font-size: 1rem;
  color: rgba(234,243,255,0.78);
  line-height: 2rem;
  max-height: 6rem;
  overflow: hidden;
  text-overflow: ellipsis;
}

.info {
  margin-top: auto;
  display: flex;
  gap: 12px;
  align-items: center;
  font-size: 0.85rem;
  color: rgba(234,243,255,0.65);
}

.rating {
  display: inline-flex;
  gap: 6px;
  align-items: center;
  background: rgba(255,255,255,0.03);
  padding: 6px 8px;
  border-radius: 999px;
  color: #ffd166;
  font-weight: 700;
}

.back {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: linear-gradient(180deg, #5a47b7, #4a3c92);
  border: 1px solid rgba(255,255,255,0.04);
  color: #eaf3ff;
  cursor: pointer;
  margin-bottom: 12px;
  padding: 6px;
}
.back:hover {
  background: rgba(124,92,255,0.12);
  transform: translateY(-2px);
}
.back svg {
  display: block;
}

@media (max-width: 600px) {
  .search-bar {
    flex-direction: column;
    align-items: stretch;
  }
  .poster {
    width: 74px;
    height: 112px;
  }
  .back {
    width: 50px;
    height: 50px;
  }
}

@media (max-width: 900px) {
  .results {
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  }
  .poster {
    width: 92px;
    height: 138px;
  }
}
</style>