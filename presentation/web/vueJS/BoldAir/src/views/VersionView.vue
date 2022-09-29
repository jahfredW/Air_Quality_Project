<template>

    <div class="hero-body is-fullheight has-text-centered"> 
        <h1 class="title has-text-centered">Version : </h1>
        <div class="columns is-flex-direction-column has-text-centered">
            <div class="column ">

              <Version
              :version="this.result['version']"
              :nom="this.result['nom']"
              :env="this.result['env']">
            </Version>
            </div>
        </div>
    </div>
</template>


<script>
import { defineComponent } from 'vue';

import Version from '../components/version.vue';
import axios from 'axios';
import countApi from 'countapi-js'
import * as countapi from "countapi-js";

export default defineComponent({
    name: 'VersionView',


  components: {
    Version,
},

  data: () => ({
    result : {},
    counter : 0,

      }),


      methods: {

      getVisit() {
        countapi.visits().then((result) => {
        console.log(result.value);
        this.counter = result.value;
        });
      },

        getEnv() {

          let self = this;
          this.error = false;
          axios.get('http://127.0.0.1:8001/environnement')
              .then((res) => {

                this.result['version'] = res.data.version
                this.result['env'] = res.data.env
                this.result['nom'] = res.data.name
                console.log(res.data)
                console.log(this.result['nom'])


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


    });

</script>