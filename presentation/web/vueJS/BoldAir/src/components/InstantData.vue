<template>
<v-container>
  <v-row class="has-text-centered" >
    <v-col cols="6">
      <div><font-awesome-icon icon="fa-solid fa-smog" class="pr-3" />
          <div> {{this.period}} </div>
          <div> {{ this.no }} </div></div>
    </v-col>
    <v-col cols="12">
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