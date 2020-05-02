<template>
    <v-app>
        <v-app-bar
                app
                color="primary"
                dark
        >
            <div class="d-flex align-center">
                <router-link to="/" class="font-weight-bolder text-white">
                    <h3>Serverless POC</h3>
                </router-link>
            </div>

            <v-spacer></v-spacer>

        </v-app-bar>

        <v-content>
            <v-container fluid>
                <router-view/>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>

    export default {
        name: 'App',

        components: {},

        data: () => ({
            //
        }),
    };
</script>

<style>
    .text-white {
        color: white !important;
        text-decoration: none !important;
    }
</style>