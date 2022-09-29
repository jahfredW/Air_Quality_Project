<template>
    <div class="doucement"> 
        <h1>Test du composant Doucement</h1>
        <div class="container mt-5">
            <DoucementCard></DoucementCard>
        </div>
        
    </div>
</template>

<script>
import { defineComponent } from 'vue';

import DoucementCard from '../components/Doucement.vue';
import {useUrlStore} from "../stores/url";

export default defineComponent({

    setup: () => {
        const store = useUrlStore()


        return {
          store
        }
      },

    name: 'DoucementView',

    components: {
        DoucementCard,
    },
});
</script>