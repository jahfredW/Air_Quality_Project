<template>
  <div class="meteo">
    <span class="title m-4">Test de notre composant MeteoCard</span>
    <MeteoCard></MeteoCard>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

// Components
import MeteoCard from '../components/MeteoCard.vue';

export default defineComponent({
  name: 'MeteoView',

  components: {
    MeteoCard,
  },
});
</script>
