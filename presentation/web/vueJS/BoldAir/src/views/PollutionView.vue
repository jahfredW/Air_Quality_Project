<template>
    <div class="meteo">
        <PollutionCard></PollutionCard>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

import PollutionCard from '../components/PollutionCard.vue';

export default defineComponent({
    name: 'PollutionView',

    components: {
        PollutionCard,
        },
    });
</script>