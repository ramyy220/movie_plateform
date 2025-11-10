<script setup>
import AppSearch from '../components/AppSearch.vue'
import MovieDiscover from '../components/MovieDiscover.vue'
</script>

<template>
  <main>
    <AppSearch />
    <MovieDiscover :count="20" />
  </main>
</template>