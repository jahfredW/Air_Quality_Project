import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import './../node_modules/bulma/css/bulma.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
library.add(fas);

const pinia = createPinia()

loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
    .use(pinia)
  .component('font-awesome-icon', FontAwesomeIcon)
  .mount('#app')
