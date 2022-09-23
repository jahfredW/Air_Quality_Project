<template>
    <v-container>
      <v-row class="mt-6 mb-2" no-gutters>
        <v-col cols="6" offset="4">
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
              {{ this.errorMessage }}
            </v-alert>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-for="card in this.cardItems">
          <Doucement 
            :period="card.period"
            :indice="card.indice"
            >
        </Doucement>
        </v-col>
      </v-row>
    </v-container>
  </template>

<script>
    import { defineComponent } from 'vue';
    
    // Components
    import Doucement from '../components/Doucement.vue';
    import axios from 'axios';
    
    export default defineComponent({
    
      components: {
        Doucement //expose le composant importé pour utilisation dans le template
      },
    
      name: "DoucementView",
      data: () => ({
        cardItems: [
          

        ],
        valid: true,
        search: '',
        searchRules: [
          v => !!v || 'Vous devez indiquer une ville pour la recherche',
          v => (v && v.length <= 20  ) || 'Le nom de la ville doit être inférieur à 20 caractères',
          v => (v[0].toUpperCase() === v[0]) && (v.slice(1) !== v.slice(1).toUpperCase()) || 'Seule la première lettre doit être en majuscule',
          
        ],
        errorMessage: '',
        error: false

    
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
    
          // on réinitialise une erreur si il y en avait une
          this.error = false;
    
          if (this.$refs.form.validate()) {
            let ville = this.search.replaceAll(' ', '+');
            console.log(ville);
            console.log('ici');
    
            axios.get('http://127.0.0.1:8001/previsions/' + ville, this.$refs.form)
              .then((res) => {
    
                // on supprime les valeurs dans le tableau cardItems

                this.cardItems = []
                
    
                // on ajoute au tableau les données reçues du backend
                for (var i in res.data) {
                  this.cardItems.push(res.data[i])
                }
    
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
                  if (error.response.status === 520) {
                    self.errorMessage = error.response.data.detail;
                    self.error = true;
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