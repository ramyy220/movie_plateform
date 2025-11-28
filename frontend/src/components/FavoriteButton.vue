<template>
  <button
    class="fav-btn"
    :class="{ active: isFavorite }"
    @click="$emit('toggle', id)"
    :aria-pressed="isFavorite"
    title="Ajouter / enlever des favoris"
  >
    <!-- simple icône coeur -->
    <svg width="20" height="20" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path
        d="M12 21s-7.5-4.953-10-8.083C-1 8.5 3.5 3 8.5 6.5 10.7 8 12 9.5 12 9.5s1.3-1.5 3.5-3C20.5 3 25 8.5 22 12.917 19.5 16.047 12 21 12 21z"
        :fill="isFavorite ? '#E53935' : 'none'"
        stroke="#ffffff"
        stroke-width="1"
        stroke-linejoin="round"
      />
    </svg>
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  id: { type: [Number, String], required: true },
  favoriteIds: { type: Array, default: () => [] }
})

const isFavorite = computed(() => {
  return Array.isArray(props.favoriteIds) && props.favoriteIds.includes(Number(props.id))
})
</script>

<style scoped>
.fav-btn {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  vertical-align: middle;
  outline: none;
  transition: transform .15s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.fav-btn:hover { transform: scale(1.05); }
.fav-btn svg { transition: fill .15s, filter .15s; }
.fav-btn.active svg { filter: drop-shadow(0 0 6px rgba(229,57,53,0.7)); }
</style>