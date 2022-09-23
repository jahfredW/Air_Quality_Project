<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list-item>
        <v-list-item-content>
            <v-list-item-title class="text-h6">
              Menu
            </v-list-item-title>
            <v-list-item-subtitle>
              Navigation
            </v-list-item-subtitle>
        </v-list-item-content>  
      </v-list-item>

      <v-list dense nav>
          <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
            <v-layout row>
              <v-flex xs1 md6 class="mr-1">
                <v-list-item-icon>
                  <v-icon large color="blue darken-2">
                    {{ item.icon}}
                  </v-icon>
                </v-list-item-icon>
              </v-flex>
              <v-flex xs11 md2 class="ml-3 pt-1">
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.title}}
                  </v-list-item-title>
                </v-list-item-content>
              </v-flex>
            </v-layout>
            </v-list-item>
            <v-divider></v-divider> 
        </v-list>
    
    </v-navigation-drawer>

    <v-app-bar id="app_bar" 
    app
    image="quino.jpg"
    density="prominent"
    bottom
    >
  
        <v-app-bar-nav-icon color="white" @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-app-bar-title class="is-size-3 has-text-centered has-text-white">Bold'Air</v-app-bar-title>
      <font-awesome-icon icon="fa-solid fa-earth-europe" class="is-size-3 mx-5" />

    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>

    <v-footer app id="footer"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
   
      <v-btn class="pl-5"
        v-for="link in links" :key="link.title" :to="link.to"
        color="white"
        rounded
        elevation="15"
        
        
      >
    
          {{ link.title }}
    
      </v-btn>
     
      <v-col
        class="primary lighten-2 py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Fg Dev</strong>
      </v-col>
      
    </v-row>
    
  </v-footer>
  </v-app>
</template>





<script>
  export default {
    name: "App",
    data: () => ({ 
      drawer: null,
      
      items: [
        {
          title: 'Rechercher>',
          icon: 'mdi-cloud-search',
          to:'/search',
        },

        {
          title: 'A propos >',
          icon: 'mdi-information',
          to: '/about',
        },

        {
          title: 'Grid-test >',
          icon: 'mdi-alert-rhombus',
          to: '/grid',
        },

      ],


      links: [
        {
          title: 'Home',
          to: '/',
        },

        {
          title: "About Us",
          to: '/',
          
        },

        {
          title: "Team",
          to: '/',
         
        },

        {
          title: "Services",
          to: '/',
         
        },

        {
          title: "Contact Us",
          to: '/',
         
        },

      ],
    }),
  }
</script>

<style>

#footer {
  background-color: #90d5d5;
}
</style>

