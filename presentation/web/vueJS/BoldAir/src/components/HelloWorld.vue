<template>
  <v-container class=" has-text-centered mt-16">
    <v-row>
      <v-col cols="12">
        <v-img
          :src="logo"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mt-15" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to the Bold' Air App !
        </h1>

          <h4>Join Us</h4>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Bold'Air developers,
          <br>please join our online
          <a
            href=""
            target="_blank"
          >Facebook Community</a>
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import logo from '../assets/Lungs.svg'

export default {
  name: 'HelloWorld',

  data: () => ({
    ecosystem: [
      {
        text: 'vuetify-loader',
        href: 'https://github.com/vuetifyjs/vuetify-loader/tree/next',
      },
      {
        text: 'github',
        href: 'https://github.com/vuetifyjs/vuetify/tree/next',
      },
      {
        text: 'awesome-vuetify',
        href: 'https://github.com/vuetifyjs/awesome-vuetify',
      },
    ],
    logo,
  }),
}
</script>
