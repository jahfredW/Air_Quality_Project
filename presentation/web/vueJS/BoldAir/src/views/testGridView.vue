<template>
    <div class="test">
        <h1>Test des composants</h1>
        <testGrid></testGrid>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

import testGrid from '../components/testGrid.vue';

export default defineComponent({
    name: 'gridView',

    components: {
    testGrid,
},
    });
</script>