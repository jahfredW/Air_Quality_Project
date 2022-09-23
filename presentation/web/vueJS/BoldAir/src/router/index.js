import { createRouter, createWebHistory } from 'vue-router'
import PollutionView from '../views/PollutionView.vue'
import MeteoView from '../views/MeteoView.vue'
import HomeView from '../views/HomeView.vue'
import ComponentView from '../views/Test.vue'
import DoucementView from '../views/Doucement.vue'
import VersionView from '../views/VersionView.vue'
import TestGridView from '../views/TestGridView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: VersionView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/searchView.vue')
    },

    {
      path: '/search',
      name: 'search',
      component: () => import ('../views/searchView.vue')
    },

    {
      path: '/grid',
      name: 'grid',
      component: () => import ('../views/TestGridView.vue')
    },
  ]
})

export default router

