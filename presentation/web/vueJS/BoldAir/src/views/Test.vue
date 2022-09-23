<template>
    <div class="test">
        <h1>Test des composants</h1>
        <TestComponents></TestComponents>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

import TestComponents from '../components/TestComponents.vue';

export default defineComponent({
    name: 'ComponentView',

    components: {
    TestComponents,
},
    });
</script>