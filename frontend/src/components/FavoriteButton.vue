<template>
  <button
    class="fav-btn"
    :aria-label="isFavorite ? 'Retirer des favoris' : 'Ajouter aux favoris'"
    @click.stop="toggle"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      :fill="isFavorite ? '#E53935' : 'none'"
      :stroke="isFavorite ? '#E53935' : '#ccc'"
      viewBox="0 0 27 27"
      width="25"
      height="25"
    >
      <path
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M12 21s-6-4.95-9-8.36C-.59 8.11 3.16 3.58 8.43 5.54A5.488 5.488 0 0 1 12 8.44c1.02-1.1 2.58-2.9 5.57-2.9 5.27-1.96 9.02 2.57 5.43 7.1C18 16.05 12 21 12 21z"
      />
    </svg>
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  id: { type: [String, Number], required: true },
  favoriteIds: { type: Array, required: true }
})

const emit = defineEmits(['toggle'])

const isFavorite = computed(() => props.favoriteIds.includes(props.id))

function toggle() {
  emit('toggle', props.id)
}
</script>

<style scoped>
.fav-btn {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  vertical-align: middle;
  outline: none;
  transition: transform .2s;
}
.fav-btn:hover svg {
  transform: scale(1.13);
  filter: drop-shadow(0 0 3px #E53935);
}
</style>