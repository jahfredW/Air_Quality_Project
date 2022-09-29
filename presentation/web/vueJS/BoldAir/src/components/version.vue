<template>
    <div class="container">
        <div class="columns is-mobile is-gapless is-flex-direction-row has-text-centered">
            <div class="column">
                <span class="icon-text">
                    <div class="columns">
                        <div class="column pt-4">
                            <font-awesome-icon icon="fa-solid fa-address-card" />
                        </div>
                        <div class="column is-narrow">
                            <div class="subtitle" >
                                nom : {{ this.nom}}
                            </div>
                        </div> 
                    </div>
                </span>
            </div>
            <div class="column">
                <span class="icon-text">
                    <div class="columns">
                        <div class="column pt-4 ">
                            <font-awesome-icon icon="fa-code-compare" />
                        </div>
                        <div class="column is-narrow">
                            <div class="subtitle">
                                version : {{this.version}}
                            </div>
                        </div>
                        
                    </div>
                </span> 
            </div>
            <div class="column">
                <span class="icon-text">
                    <div class="columns">
                        <div class="column pt-4 "> 
                            <font-awesome-icon icon="fa-solid fa-gears"/>
                        </div>
                        <div class="column is-narrow">
                            <div class="subtitle">
                                environnement : {{ this.env}}
                            </div>
                        </div>
                    </div>
                </span>
            </div>
        </div>
    </div>

</template>

<script>
    export default {

        data: () => ({


        }),

        props: {
          nom: String,
          version: Number,
          env: String,
        },


        computed: {

        }
    }

</script>