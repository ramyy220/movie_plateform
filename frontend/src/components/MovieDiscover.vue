<template>
  <div class="layout">
    <aside class="sidebar">
      <FilterMovie v-model="filter" />
    </aside>

    <section class="discover">
      <h2>Découvertes</h2>

      <div v-if="loading" class="loading">Chargement...</div>
      <div v-if="error" class="error">{{ error }}</div>

      <div v-if="movies.length" class="grid">
        <article v-for="m in movies" :key="m.id" class="card">
          <img
            :src="posterUrl(m.poster_path)"
            :alt="m.title"
            class="poster"
            loading="lazy"
          />
          <div class="meta">
            <h3 class="title">{{ m.title }}</h3>
            <div class="info">
              <span class="rating">⭐ {{ m.vote_average ?? '—' }}</span>
            </div>
            <p class="info">{{ m.release_date ? m.release_date.slice(0,4) : '—' }}</p>
          </div>
        </article>
      </div>

      <button v-if="!loading && page < total_pages" @click="loadMore" class="more">
        Charger plus
      </button>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { discoverMovies, nowplayingMovies, moviePopular, movieTopRated, movieUpcoming } from '../services/movieService' 
import FilterMovie from './FilterMovie.vue'

const props = defineProps({
  count: { type: Number, default: 12 },
  initialPage: { type: Number, default: 1 }
})

const movies = ref([])
const page = ref(props.initialPage)
const total_pages = ref(1)
const loading = ref(false)
const error = ref(null)

const filter = ref(null)

const TMDB_IMG = 'https://image.tmdb.org/t/p/w342'

function posterUrl(path) {
  return path ? (TMDB_IMG + path) : '/img/no-poster.png'
}

async function fetchMovies(p = 1) {
  loading.value = true
  error.value = null
  try {
    let data
    // si le filtre est now_playing, utiliser nowplayingMovies
    if (filter.value === 'now_playing') {
      data = await nowplayingMovies({ page: p, count: props.count })
    } else if (filter.value === 'popular') {
      data = await moviePopular({ page: p, count: props.count })
    } else if (filter.value === 'top_rated') {
      data = await movieTopRated({ page: p, count: props.count })
    } else if (filter.value === 'upcoming') {
      data = await movieUpcoming({ page: p, count: props.count })
    } else {
      data = await discoverMovies({ page: p, count: props.count })
    }

    if (data.results) {
      if (p === 1) movies.value = data.results
      else movies.value = movies.value.concat(data.results)
      page.value = data.page || p
      total_pages.value = data.total_pages || 1
    } else {
      throw new Error('Réponse inattendue du serveur')
    }
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

function loadMore() {
  if (page.value >= total_pages.value) return
  fetchMovies(page.value + 1)
}

watch(filter, () => {
  page.value = 1
  fetchMovies(1)
})

onMounted(() => {
  console.debug('[MovieDiscover] mounting, initial page =', page.value)
  fetchMovies(page.value)
})
</script>

<style scoped>
.layout {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  padding: 20px;
  box-sizing: border-box;
}

.discover {
  flex: 1;
  width: 100%;
  margin: 0;
  box-sizing: border-box;
}

.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 25px;
  margin-top: 16px;
}

.card {
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
  font-size: 0.88rem;
  color: rgba(234,243,255,0.78);
  line-height: 1.3;
  max-height: 3.3em;
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

.more {
  margin: 24px auto;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  color: #eaf3ff;
  background-color: #2a293a;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.sidebar {
  position: relative;
  width: 270px;
  padding: 15px;
  background: #1e1e2f;
  border-radius: 12px;
  box-shadow: 0 8px 28px rgba(2,6,23,0.45);
  margin: 0;
  margin-top: 20px;
}

@media (max-width: 900px) {
  .layout {
    flex-direction: column;
    gap: 16px;
  }
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .poster {
    width: 92px;
    height: 138px;
  }
  .discover {
    margin-left: 0;
  }
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
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>