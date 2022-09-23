<template>
    <div class="hero-body is-fullheight has-text-centered"> 
        <h1 class="title has-text-centered">Version : </h1>
        <div class="columns is-flex-direction-column has-text-centered">
            <div class="column "><Version></Version></div> 
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

import Version from '../components/version.vue';
import Doucement from './Doucement.vue';

export default defineComponent({
    name: 'VersionView',

    components: {
    Version,
},
});
</script>