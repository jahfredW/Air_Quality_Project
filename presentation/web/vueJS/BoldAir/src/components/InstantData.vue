<template>

  <v-card
    class="mx-auto my-12 has-text-centered"
    max-width="80%"
    shaped
    elevation="19"
  >
    <v-banner v-if="this.polluantArray.length >= 0" class="title  pl-13 pr-3 is-size-5-tablet is-size-7-mobile
is-size-3-desktop" elevation="19">
      <v-row>
          <v-col cols="4">
            {{ this.toDate() }}
          </v-col>
          <v-col cols="5" class="title pb-5 has-text-centered pr-0 pl-15">
            <strong class="has-text-success is-size-5-tablet is-size-7-mobile is-size-3-desktop">AQI : {{ polluantArray[0]['aqi']}}</strong>
          </v-col>
          <v-col cols="3" class="title pb-5 has-text-left pr-12">
            <strong><v-img width="30%"  :src="logoCorrect"></v-img></strong>
          </v-col>
        </v-row>
    </v-banner>

    <v-banner elevation="9" class="mb-2">
      <v-row>
      <v-col border="top" cols="2" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop">
        Polluant
      </v-col>
      <v-col cols="2" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop">taux µg/m3 </v-col>
      <v-col cols="2" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop">Smil'Air</v-col>
      <v-col cols="2" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop ml-4">%(instant) </v-col>
        <v-col cols="3" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop ml-1">Prev Semaine </v-col>
      </v-row>
    </v-banner>
    <v-template v-for="(pol,index) in polluantArray[0]">
      <v-banner v-if="index !== 'aqi' && index !== 'no' " elevation="15" rounded class="mb-2">
          <v-row >
          <v-col cols="2" class="subtitle pt-9">
            <a v-if="index === 'no2'" :href=(this.selectAllOptions(index,pol))[1]
                                              target="_blank"
                                              :title="this.selectAllOptions(index, pol)[0]">
              NOx </a>
            <a v-else :href=(this.selectAllOptions(index,pol))[1]
                                              target="_blank"
                                              :title="this.selectAllOptions(index, pol)[0]">
              {{ index.toUpperCase() }}</a></v-col>

          <v-col v-if="index ==='no2'" cols="2" class="subtitle pt-9">{{Math.ceil(parseFloat(pol) + parseFloat(polluantArray[0]['no'])) }}</v-col>
           <v-col v-else cols="2" class="subtitle pt-9">{{ pol }}</v-col>
          <v-col cols="2" class="mx-2 pt-5 "><v-img width="60%"  :src="this.selectAllOptions(index, pol)[2]"></v-img> </v-col>
          <v-col cols="2" class="mt-1">

            <v-progress-circular
                  v-model= "this.selectAllOptions(index, pol)[3]"
                  color="#80aaff"
                  size="70"
                  width="7"
                  class="is-size-6-tablet is-size-7-mobile is-size-5-desktop mt-1"

                  >
                <template v-slot:default="{ value }">
            <strong>{{ this.selectAllOptions(index, pol)[3] }}%</strong>

          </template>
              </v-progress-circular>

            </v-col>
          <v-col cols="3" class="is-size-5-tablet is-size-7-mobile is-size-4-desktop mt-0 pt-9">
          <v-btn
            color="#e6b3ff"
            text
            height="30"

          >
            <strong >Cliquez</strong>
          </v-btn>
          </v-col>

        </v-row>
        </v-banner>
    </v-template>



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
  data() {
    return {
      imagePollution,
      logoGood,
      logoCorrect,
      logoMediocre,
      logoDegrade,
      logoMauvais,

      loading: false,
      selection: 1,
      v: 0,
      nom: "",
      aqi: 'co',
      urlListe: [ "https://fr.wikipedia.org/wiki/Indice_de_qualit%C3%A9_de_l%27air",
     "https://fr.wikipedia.org/wiki/Monoxyde_de_carbone",
          "https://fr.wikipedia.org/wiki/Ammoniac",
        "https://environnement.public.lu/fr/loft/air/Polluants_atmospheriques/les_oxydes_d_azote_NOx.html",]

    }
    },



  props : {
        polluantArray: Array,
    },

  methods: {

      selectAllOptions(name, pol) {
        let nom = ""
        let url = ""
        let logo = ""
        let taux = -1;
        switch (name) {
          case "aqi":
            nom = "Indice de qualité de l'air";
            url = this.urlListe[0];
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
            break;
          case "co":
            nom = "Monoxyde de Carbone";
            taux = this.calculTaux(name);
            url = this.urlListe[1];
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
            break;
          case "nh3":
            nom = "Ammoniac";
            taux = this.calculTaux(name)
            url = this.urlListe[2];
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
            break;
          case "no":
            nom = "Monoxyde d'azote";
            taux = this.calculTaux(name);
            url = "";
            break;
          case "no2":
            nom = "Dioxyde d'azote";
            url = this.urlListe[3];
            taux = this.calculTaux(name);
            let nox = parseFloat(pol) + parseFloat(this.polluantArray[0]['no']);
            console.log(nox)
            if ( nox <= 5) {
              logo = logoGood
            } else if ( nox > 5 && nox <= 10) {
              logo = logoCorrect
            } else if ( nox > 10 && nox <= 20) {
              logo = logoMediocre
            } else if (nox > 20 && nox <= 30) {
              logo = logoMauvais
            } else {
              logo = logoDegrade
            }
            break;
          case "o3":
            nom = "Ozone";
            url = "";
            taux = this.calculTaux(name);
            logo = logoGood
            break;
          case "so2":
            nom = "Soufre";
            url = "";
            logo = logoCorrect;

              taux = this.calculTaux(name);

            break;
          case "pm25":
            nom = "Microparticules < 2.5 µm";
            url = "";
            logo = logoCorrect;
            taux = this.calculTaux(name);
            break;
          case "pm10":
            nom = "Microparticules < 10 µm";
            url = "";
            taux = this.calculTaux(name);
            logo = logoCorrect;
            break;
          default:
            nom = "caca";
        }
        return [nom, url, logo, taux]
      },

      calculTaux(polluant) {
            let taux = 0;
            let maxCo = 300;
            let data = this.polluantArray[0][polluant];
            switch (polluant) {
              case 'co':
                taux = data / 30;
                break;
              case 'nh3':
                taux = data / 170;
                break;
              case 'no2':
                taux = ( 10 * data ) / 4;
                break;
              case 'o3':
                taux = ( 10 * data ) / 12;
                break;
              case 'no':
                taux = data / 310;
                break;
              case 'pm10':
                taux = data / 1.5;
                break;
              case 'pm25':
                taux = data / 0.33;
                break;
              case 'so2':
                taux = data / 1.25;
                break;
            }

            return Math.ceil(taux)

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
.v-progress-circular__bar, .v-progress-linear__bar__determinate {
  transition: none;
}

</style>