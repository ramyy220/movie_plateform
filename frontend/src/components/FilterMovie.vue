<template>
  <div class="filters">
    <h2>Filtres</h2>
    <button
      v-for="f in filters"
      :key="f.key"
      :class="{ active: selected === f.key }"
      @click="selectFilter(f.key)"
      type="button"
    >
      {{ f.label }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'FilterMovie',
  props: {
    modelValue: {
      type: String,
    },
    filters: {
      type: Array,
      default: () => [
        { key: 'now_playing', label: 'Now Playing' },
        { key: 'popular', label: 'Populaire' },
        { key: 'top_rated', label: 'Top Rated' },
        { key: 'upcoming', label: 'À venir' }
      ]
    }
  },
  emits: ['update:modelValue', 'change'],
  data() {
    return {
      selected: this.modelValue
    }
  },
  watch: {
    modelValue(v) {
      this.selected = v
    }
  },
  methods: {
    selectFilter(key) {
      if (this.selected === key) return
      this.selected = key
      this.$emit('update:modelValue', key) 
      this.$emit('change', key)       
    }
  }
}
</script>

<style scoped>
h2 {
  margin-bottom: 12px;
  font-weight: 600;
  text-align: center;
}
.filters {
  display: grid;
  gap: 20px;
}
.filters button {
  padding: 15px 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  background: white;
  cursor: pointer;
  border-radius: 8px;
}
.filters button.active {
  background: linear-gradient(180deg, #5a47b7, #4a3c92);
  color: white;
  border-color: rgba(255,255,255,0.1);}
</style>