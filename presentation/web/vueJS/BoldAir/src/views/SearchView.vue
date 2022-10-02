<template>
    <v-container>
      <v-row class="mt-6 mb-2 " no-gutters >
        <v-col cols="6" offset="4" class="pl-6">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row no-gutters>
              <v-col>
                <v-text-field :rules="searchRules" v-model="search" @keydown.enter.prevent="submit" required
                  placeholder="Rechercher une ville..." prepend-inner-icon="mdi-map-search" variant="solo" dense rounded
                  single-line></v-text-field>
              </v-col>
              <v-col class="px-1 mt-1">
                <v-btn color="success" size="x-large" @click="submit">
                  <v-icon size="large" dark>
                    mdi-cloud-search
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6" offset="3">
          <div>
            <v-alert v-model="error" variant="outlined" type="info" prominent border="top" @click="this.error = false; ">
              {{ this.message }}
            </v-alert>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-if="loading" cols="12">
          <Loading></Loading>
        </v-col>
        <v-col v-for="card in this.cardItems">
          <Doucement
            :period="card.period"
            :indice="card.indice"
            :description="card.description"
            >
        </Doucement>
        </v-col>
      </v-row>
    </v-container>
  </template>

<script>
    import { defineComponent } from 'vue';
    import { useUrlStore } from "../stores/url";


    // Components
    import Doucement from '../components/Doucement.vue';
    import InstantData from "../components/InstantData.vue";
    import Loading from "../components/loading.vue";
    import axios from 'axios';


    export default defineComponent({

      setup: () => {
        const store = useUrlStore()
        const urlMain = store.urlMain
        const ipMain = store.ipMain
        const portMAin = store.portMain

        return {
          urlMain, ipMain, portMAin
        }
      },

      components: {
        InstantData,
        Loading,
        Doucement //expose le compé pour utilisation dans le template
      },

      name: "DoucementView",

      data: () => ({
        cardItems: [
        ],
        loading: false,
        valid: true,
        search: '',
        searchRules: [
          v => !!v || 'Vous devez indiquer une ville pour la recherche',
          v => (v && v.length <= 20  ) || 'Le nom de la ville doit être inférieur à 20 caractères',
          v => (v[0].toUpperCase() === v[0]) && (v.slice(1) !== v.slice(1).toUpperCase()) || 'Première en majuscule, le reste en minuscule',

        ],
        errorMessage: '',
        error: false,
        message: ''
      }),

      methods: {

        submit() {

          // technique pour éviter les problèmes lors des appels asynchrones avec
          // avec la librairie Axios.
          // lors de l'utilisation de fonction javascripts flechés, le mot clé this
          // représente alors la fonction et non plus le composant vuejs lui-même.
          //
          // ce qui pose problème lorsqu'on veut mettre à jour des données du composant.
          // c'est pourquoi on crée un variable qui sert de référence au composant.
          let self = this;
          this.cardItems = [];

          // on réinitialise une erreur si il y en avait une
          this.error = false;

          if (this.$refs.form.validate() && ( this.search[0].toUpperCase() === this.search[0]
          && this.search.slice(1) === this.search.slice(1).toLowerCase())) {
            this.loading = true;
            let ville = this.search.replaceAll(' ', '+');

            var formData = new FormData();
            formData = {ville}
            axios.post("http://" + this.ipMain + ":" + this.portMAin + "/previsions", formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            })
              .then((res) => {

                // on supprime les valeurs dans le tableau cardItems

                this.cardItems = []
                console.log(res.data)
                this.loading = false


                // on ajoute au tableau les données reçues du backend
                for (var i in res.data) {
                  this.cardItems.push(res.data[i])
                }

                console.log(this.cardItems)

              })
              .catch(function (error) {
                if (error.response) {
                  // The request was made and the server responded with a status code
                  // that falls out of the range of 2xx
                  console.log(error.response.data);
                  console.log(error.response.status);
                  console.log(error.response.headers);

                  // Si c'est une erreur 520, il a été définit que ce sont des informations d'erreur
                  // envoyées par le back.
                  // Nous pouvons donc l'utiliser pour afficher le message à l'utilisateur
                  if (error.response.status === 500) {

                    self.errorMessage = error.response.data.detail;
                    self.error = true;
                    self.message = "La ville n'existe pas ! Réessaie ! "
                    this.loading = false;


                  }

                } else if (error.request) {
                  // The request was made but no response was received
                  // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                  // http.ClientRequest in node.js
                  console.log(error.request);
                } else {
                  // Something happened in setting up the request that triggered an Error
                  console.log('Error', error.message);
                }
                console.log(error.config);
              })
          }
        },

      },

    })
    </script>
    
    
  
  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>