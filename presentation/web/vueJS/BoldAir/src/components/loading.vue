<template>
  <div class="has-text-centered mt-5">
    {{ this.setShow() }}
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

    props : {
      show: Boolean
    },

    methods: {
      setShow() {
        setTimeout(() => {
          this.show = false;
        }, 4500);

      },


    }
  }
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>