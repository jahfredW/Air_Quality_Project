<template>
    <div class="card meteo_card mx-4">
        <div class="card-header">
            <div class="card-header-title">{{ this.dayFromPeriod }}</div>
            <div class="card-header-icon">
               <!-- pas d'icone d'en tête pour le moment -->
            </div>
        </div>
        <div class="py-6 meteo_card_picture">
            <div class="has-text-centered">
                <v-img v-if="this.weatherStatus === this.STATUT_API_NUAGEUX" :src="logoNuage" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_PARTIELLEMENT_NUAGEUX" :src="logoSoleilNuage" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_PEU_NUAGEUX" :src="logoNuage" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_CIEL_DEGAGE" :src="logoSoleil" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_LEGERE_PLUIE" :src="logoPluie" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_BRUME" :src="logoBrume" class="fa-4x" contain height="200" />
                <v-img v-else-if="this.weatherStatus === this.STATUT_API_LEGERE_COUVERT" :src="logoCouvert" class="fa-4x" contain height="200" />
                <font-awesome-icon v-else icon="fas fa-circle-question" class="fa-4x has-text-warning" />
            </div>
            <p class="title is-1 has-text-white has-text-centered mt-2">{{ this.temperature }}°</p>
        </div>
        <div class="card-content">
            <div class="columns is-mobile is-gapeless">
                <div class="column">
                    <p>{{ this.weatherStatus }}</p>
                </div>
                <div class="column">
                    <span class="icon-text">
                        <div class="columns is-gapless">
                            <div class="column">
                                <font-awesome-icon icon="fa-wind"></font-awesome-icon>
                                <span class="icon">
                                    <i class="fas fa-wind"></i>
                                </span>
                            </div>
                            <div class="column">
                                <span>{{ this.forceVent }} Km/h</span>
                            </div>
                        </div>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import logoSoleil from '../assets/soleil.svg'
import logoSoleilNuage from '../assets/soleil-nuage.svg'
import logoPluie from '../assets/pluie.svg'
import logoNuage from '../assets/nuageux.svg'
import logoBrume from '../assets/brume.svg'
import logoCouvert from '../assets/couvert.svg'


export default {

    data: () => ({

        STATUT_API_NUAGEUX: "nuageux",
        STATUT_API_PEU_NUAGEUX: "peu nuageux",
        STATUT_API_PARTIELLEMENT_NUAGEUX: "partiellement nuageux",
        STATUT_API_CIEL_DEGAGE: "ciel dégagé",
        STATUT_API_LEGERE_PLUIE: "légère pluie",
        STATUT_API_LEGERE_COUVERT: "couvert",
        STATUT_API_BRUME: "brume",

        temperature: 19,
        forceVent: 18,
        weatherStatus: "ciel dégagé",
        period: 0,
        logoSoleil,
        logoBrume,
        logoNuage,
        logoPluie,
        logoSoleilNuage,
        logoCouvert,
    }),


    computed: {
        dayFromPeriod() {

            if (this.period === -1) return "jour non défini.";
            if (this.period < -1 || this.period > 7) return "Période incorrecte";

            //on obtient la date en fonction de la période (J+1, J+2 etc...)
            const today = new Date();
            const dateFromPeriod = new Date();
            dateFromPeriod.setDate(today.getDate() + this.period);

            //on construit le tableau des jours de la semaine pour obtenir
            //la chaine de caractère à retourner
            let jours_semaine = ["Dimanche", "Lundi", "Mardi", "Mercred", "Jeudi", "Vendredi", "Samedi"];

            return jours_semaine[dateFromPeriod.getDay()];
        },
    },
}

</script>


<style>
.meteo_card_picture {
    background: linear-gradient(to bottom, #72EDF2AA 0%, #5151E5BC 80%), url('https://images.unsplash.com/photo-1559963110-71b394e7494d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80') right center no-repeat;
}

.meteo_card {
    border-radius: 0.8rem;
}
</style>