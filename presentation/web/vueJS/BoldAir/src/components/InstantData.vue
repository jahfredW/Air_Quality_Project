<template>

  <v-card

    class="mx-auto my-12 has-text-centered"
    max-width="80%"
    shaped

    elevation="19"
  >

    <!--
    <v-img v-if="polluantArray.length > 0"
      height="250"
      :src="imagePollution"
      class="my-10"
    ></v-img>
    -->
    <v-card-title v-if="this.polluantArray.length >= 0" class="title mt-5">{{ this.toDate() }}</v-card-title>
    <v-divider></v-divider>
    <v-row v-for="(pol,index) in polluantArray[0]">
      <v-col cols="2" class="subtitle"><a href="https://fr.wikipedia.org/wiki/Monoxyde_de_carbone"
                                          target="_blank" :title="this.nomPolluant(index)">{{ index.toUpperCase() }}</a></v-col>
      <v-col cols="2" class="subtitle">{{ pol }}</v-col>
      <v-col cols="1" class="mx-2"><v-img width="60%"  :src="this.logoAqi(index, pol)"></v-img> </v-col>
      <v-col cols="3" class="mt-0">
          <v-progress-linear
      v-model="power"
      color="#8080ff"
      height="30"


    >
            <template v-slot:default="{ value }">
        <strong>{{ pol }}%</strong>
      </template>
          </v-progress-linear>
        </v-col>
      <v-col cols="3" class="mt-0">
      <v-btn
        color="#e6b3ff"
        text
        @click="reserve"
        height="30"

      >
        <strong >Previsions</strong>
      </v-btn>
      </v-col>
      <v-divider class="mx-4"></v-divider>
    </v-row>

  </v-card>
</template>

<script>

import imagePollution from '../assets/pollutionTest.jpg'
import axios from "axios";

    import logoGood from '../assets/good.svg'
    import logoCorrect from '../assets/correct.svg'
    import logoMediocre from '../assets/mediocre.svg'
    import logoDegrade from '../assets/degrade.svg'
    import logoMauvais from '../assets/mauvais.svg'

export default {
  name: "InstantData",
  data: () => ({
    imagePollution,
    logoGood,
    logoCorrect,
    logoMediocre,
    logoDegrade,
    logoMauvais,
      skill: 70,

      knowledge: 55,
      power: 100,
      rating: 2,
    loading: false,
    selection: 1,
    nom : "",


    }),

  props : {

        period: Number,
        polluant: String,
        polluantArray: Array,

    },

  methods: {
      reserve() {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },

      logoAqi(index, pol) {
        let logo = "";
        if (index === "aqi") {
          switch (pol) {
            case 1:
              logo = logoGood;
              break;
            case 2:
              logo = logoCorrect;
              break;
            case 3:
              logo = logoMediocre;
              break;
            case 4:
              logo = logoDegrade;
              break;
            case 5:
              logo = logoMauvais;
              break;
            default:
              logo = logoGood;
          }
        }
        else if (index === "co") {
            if ( pol <= 200) {
              logo = logoGood
            } else if ( 200 < pol <= 400) {
              logo = logoCorrect
            } else if (400 < pol <= 600) {
              logo = logoMediocre
            } else if (600 < pol <= 800) {
              logo = logoMauvais
            } else {
              logo = logoDegrade
            }

          }
          return logo

      },

      nomPolluant(name) {
        switch (name) {
          case "aqi":
            this.nom = "Indice de qualité de l'air";
            break;
          case "co":
            this.nom = "Monoxyde de Carbone";
            break;
          case "nh3":
            this.nom = "Ammoniac";
            break;
          case "no":
            this.nom = "Monoxyde d'azote";
            break;
          case "no2":
            this.nom = "Dioxyde d'azote";
            break;
          case "o3":
            this.nom = "Ozone";
            break;
          case "so2":
            this.nom = "Soufre";
            break;
          case "pm25":
            this.nom = "Microparticules < 2.5 µm";
            break;
          case "pm10":
            this.nom = "Microparticules < 10 µm";
            break;
          default:
            this.nom = "caca";
        }
        return this.nom
      },

        toDate() {
          if (this.polluantArray.length > 0) {
            const timestamp = new Date().getTime();
            let date = new Date(timestamp)
            let dateStr = date.toString()
            return dateStr.slice(0, 25)
          }

        },
      }





}
</script>

<style scoped>

</style>