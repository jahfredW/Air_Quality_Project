<template>
  <Menu>Hello</Menu>
</template>

<script>
import { defineComponent } from 'vue';

// Components
import Menu from '../components/Menu.vue';

export default defineComponent({
  name: 'MenuView',

  components: {
    Menu,
  },
});
</script>
