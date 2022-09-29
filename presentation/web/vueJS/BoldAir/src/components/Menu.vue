<template>
    <v-navigation-drawer
        app
      v-model="drawer"
    >
      <v-list-item>
        <v-list-item-content>
            <v-list-item-title class="text-h6">
              Previsions
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
                    {{ item.icon }}
                  </v-icon>
                </v-list-item-icon>
              </v-flex>
              <v-flex xs11 md2 class="ml-3 pt-1">
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.title }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-flex>
            </v-layout>
            </v-list-item>
            <v-divider></v-divider>
        </v-list>
    </v-navigation-drawer>

</template>

<script>
export default {
  name: "Menu",

  data: () => ({
    drawer: null,

    items: [
      {
        title: 'prévisions détaillées du jour>',
        icon: 'mdi-cloud-search',
        to: '/search',
      },

      {
        title: 'prévisions détaillées J+5 >',
        icon: 'mdi-information',
        to: '/about',
      },

      {
        title: 'recherche par polluants >',
        icon: 'mdi-alert-rhombus',
        to: '/test',
      },

    ],
  })

}

</script>

<style scoped>

</style>