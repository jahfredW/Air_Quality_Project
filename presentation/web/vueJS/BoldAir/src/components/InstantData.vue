<template>
<v-container>
  <v-row class="has-text-centered" >
    <v-col>
      <div><font-awesome-icon icon="fa-solid fa-smog" class="pr-3" />
          <strong> {{this.period}} : {{ this.no }} </strong></div>
    </v-col>
    <v-col class="ml-6">
      <v-progress-circular
      v-model="no"
      color="#ccb3ff"
      :size="50"
      :width="5">
      <template v-slot:default="{ value }">
        <strong>{{ Math.ceil(value) }}</strong>
      </template>
    </v-progress-circular>
    </v-col>
    <v-col class="pt-0 mx-10">
      <v-rating
      v-model="rating"
      background-color="purple lighten-3"
      color="purple"
      large
    ></v-rating>
    </v-col>
  </v-row>
  <v-divider></v-divider>

</v-container>
</template>

<script>
export default {
  name: "InstantData",
  data: () => ({
      skill: 70,
      knowledge: 55,
      power: 100,
      rating: 2,
    }),

  props : {

        period: Number,
        no: String,
        no2: String,
        pm2_5: Number,
        description: String,

    },



}
</script>

<style scoped>

</style>