<template>
  <div class="has-text-centered mt-5">
    <v-progress-circular
      indeterminate
      color="#dd99ff"
      :size="90"
    ></v-progress-circular>
  </div>

</template>


<script>
  export default {
    name: "loading",

    data() {
      return {
        show: true,
      };
    },

  }
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>