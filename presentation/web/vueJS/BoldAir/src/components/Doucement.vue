<template>
   <div class="card meteo_card mx-4">
        <div class="card-header">
            <div class="card-header-title">{{ this.dayFromPeriod }}</div>
            <div class="card-header-icon">
                <font-awesome-icon icon="fas fa-lungs"  ></font-awesome-icon>
            </div>
        </div>
        <div class="py-6 meteo_card_picture">
            <div class="has-text-centered">
                <v-img v-if="this.description === this.STATUT_API_BON" :src="logoGood" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.description === this.STATUT_API_CORRECT" :src="logoCorrect" class="fa-4x" contain height="200"/>
                <v-img v-else-if="this.description === this.STATUT_API_MEDIOCRE" :src="logoMediocre" class="fa-4x" contain height="200"/>
                <v-img v-else-if="this.description === this.STATUT_API_DEGRADE" :src="logoDegrade" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.description === this.STATUT_API_MAUVAIS" :src="logoMauvais" class="fa-4x" contain height="200" />
                <font-awesome-icon v-else icon="fas fa-circle-question" class="fa-4x has-text-warning" />
            </div>
            <p class="title is-1  has-text-centered mt-2">{{ this.indice }}</p>
        </div>
        <div class="card-content">
            <div class="columns is-mobile is-gapless">
                <div class="column has-text-centered">
                    <p>{{ this.description}}</p>
                </div>  

            </div>
        </div>
    </div> 
</template>

<script>
    import logoGood from '../assets/good.svg'
    import logoCorrect from '../assets/correct.svg'
    import logoMediocre from '../assets/mediocre.svg'
    import logoDegrade from '../assets/degrade.svg'
    import logoMauvais from '../assets/mauvais.svg'


    export default {

        name : "Doucement",

        data: () => ({
            STATUT_API_BON : "Qualité de l'air excellente !",
            STATUT_API_CORRECT: "Qualité de l'air convenable",
            STATUT_API_MEDIOCRE: "Qualité de l'aire médiocre..",
            STATUT_API_DEGRADE: "Qualité de l'air dégradée !",
            STATUT_API_MAUVAIS: "Alerte Pollution !",

            INDICE_BON : 1,
            INDICE_CORRECT: 2,
            INDICE_MEDIOCRE: 3,
            INDICE_DEGRADE: 4,
            INDICE_MAUVAIS: 5,

        
         
            logoGood,
            logoCorrect,
            logoMediocre,
            logoDegrade,
            logoMauvais,
        
        }
        ),

        props : {
            
        indice: Number,
        period: Number,
        pm2_5: Number,
        description: String,
      
    },

        computed: {
            dayFromPeriod() {
                
                if (this.period === -1) return "jour non défini";
                if (this.period < -1 || this.period > 7) return "Période Incorrecte";

                const today = new Date();
                const dateFromPeriod = new Date();
                dateFromPeriod.setDate(today.getDate() + this.period);

                let weekDays = [
                    "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi",
                    "Vendredi", "Samedi", 
                ];

                return weekDays[dateFromPeriod.getDay()];
            },

    }
}

</script>

<style>
.meteo_card_picture
{
    background: linear-gradient(to bottom, #72EDF2AA 40%, #5151E5BC 90%), url('../assets/pollutionTest.jpg')  center /auto no-repeat;
}

.meteo_card {
    border-radius: 0.8rem;
}
</style>
