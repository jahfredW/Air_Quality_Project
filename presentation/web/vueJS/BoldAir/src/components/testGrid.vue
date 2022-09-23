<template>
    
        <v-container>
      <v-row class="mt-6 mb-2" no-gutters>
        <v-col cols="6" offset="4">
          <v-form ref="form" >
            <v-row no-gutters>
              <v-col>
                <v-text-field 
                  placeholder="Rechercher une ville..." prepend-inner-icon="mdi-map-marker" variant="solo" dense rounded
                  single-line></v-text-field>
              </v-col>
              <v-col class="px-1 mt-1">
                <v-btn color="success" size="x-large" >
                  <v-icon size="large" dark>
                    mdi-cloud-search
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6" offset="3">
          <div>
            <v-alert >
              HEy
            </v-alert>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-for="card in this.cardItems">
          <PollutionCard :period="card.period"
            :indice="card.indice"
            :pollutionStatus="card.pollutionStatus">
        </PollutionCard>
        </v-col>
      </v-row>
    </v-container>
 </template>  
    



<!--
<v-container>
        <v-row no-gutters>
            <v-col cols="5" offset="3">
                <v-form ref="form">
                    <v-row  class="is-flex-direction-row">
                        <v-col  >
                            <v-text-field 
                            placeholder="Rechercher Une Ville..."
                            variant="solo"
                            single-line
                            dense
                            rounded><v-icon>
                                    mdi-access-point
                                </v-icon></v-text-field>
                        </v-col >
                        <v-col class="pt-3 ">
                            <v-btn size="x-large" class=" has-background-success">
                                <v-icon>
                                    mdi-cloud-search
                                </v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-form>
            </v-col>  
        </v-row>
    </v-container>
</template>
-->
    