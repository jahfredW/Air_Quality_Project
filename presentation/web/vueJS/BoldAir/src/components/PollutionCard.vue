<template>
    <div class="hero is-fullheight">
        <div class="hero-header">
        </div>
        <div class="hero-body py-6 bg-img has-text-centered ">
            <div class="container has-text-centered ">
                <div class="title is-1 has-text-white">
                    Bienvenue sur L'application Bold'Air
                </div>
                <div class="subtitle">
                    Pour connaitre la qualité de l'air dans ta ville
                </div>
            </div>
        </div>
        <div class="hero-foot px-2">
            <!--
            <div class="columns is-mobile is-gapeless">
                <div class="column">
                    <p>Frédéric Gruwé</p>
                    <p>Développement</p>
                </div>
                <div class="column has-text-right">
                    <span class="icon-text">
                        <div class="columns is-gapless is-flex-direction-column">
                            <div class="column">
                                <span>
                                <font-awesome-icon icon="fa-poo"></font-awesome-icon>
                                </span>
                            </div>
                            <div class="column">
                                    <span>version1.0
                                    </span>
                            </div>
                        </div>
                    </span>
                </div>
            </div>
        -->
        </div>
    </div>
</template>

<script>
import logoGood from '../assets/good.svg'
import logoSoleilNuage from '../assets/soleil-nuage.svg'
import logoPluie from '../assets/pluie.svg'
import logoNuage from '../assets/nuageux.svg'
import logoBrume from '../assets/brume.svg'
import logoCouvert from '../assets/couvert.svg'
import logoPollution from '../assets/pollution.svg'


export default {

    data: () => ({

        STATUT_API_GOOD: "good",
        STATUT_API_PEU_NUAGEUX: "peu nuageux",
        STATUT_API_PARTIELLEMENT_NUAGEUX: "partiellement nuageux",
        STATUT_API_CIEL_DEGAGE: "ciel dégagé",
        STATUT_API_LEGERE_PLUIE: "légère pluie",
        STATUT_API_LEGERE_COUVERT: "couvert",
        STATUT_API_CORRECT: "correcte",

        
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
            let jours_semaine = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"];

            return jours_semaine[dateFromPeriod.getDay()];
        },
    },
}

</script>


<style>


.bg-img
{
    background: linear-gradient(to bottom, #72EDF2AA 40%, #5151E5BC 90%), url('../assets/pollutionTest.jpg')  center no-repeat;
}

.meteo_card {
    border-radius: 0.8rem;
}
</style>