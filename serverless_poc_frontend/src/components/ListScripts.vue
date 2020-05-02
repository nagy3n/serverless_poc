<template>
    <div>
        <v-toolbar flat color="white">
            <v-toolbar-title>Script list</v-toolbar-title>
            <v-spacer/>
            <v-btn color="primary" dark :to="{ name: 'add-script' }">
                Add
            </v-btn>
        </v-toolbar>

        <v-data-table
                :headers="headers"
                :items="scripts"
                :items-per-page="5"
                class="elevation-1"
        >
            <template v-slot:item.name="{ item }">
                {{item}}
            </template>
            <template v-slot:item.execute="{ item }">
                <v-btn
                        small
                        color="primary"
                        :to="{ name: 'execute-script', params: { scriptName: item } }"
                >
                    Execute
                </v-btn>
            </template>
            <template v-slot:item.delete="{ item }">
                <v-btn
                        small
                        color="primary"
                        @click="deleteScript(item)"
                >
                    delete
                </v-btn>
            </template>
        </v-data-table>
    </div>
</template>

<script>
    import {HTTP} from "../utils";

    export default {
        name: "ListScripts",
        data: () => ({
            headers: [
                {
                    text: 'Script name',
                    value: 'name',
                },
                {
                    text: 'Execute',
                    value: 'execute',
                },
                {
                    text: 'Delete',
                    value: 'delete',
                },
            ],
            scripts: []
        }),
        mounted() {
            this.getScripts()
        },
        methods: {
            deleteScript(scriptName) {
                HTTP.delete(`/delete_script/${scriptName}`).then(() => this.getScripts())
            },
            getScripts() {
                HTTP.get('/').then(res => this.scripts = res.data)
            }
        },
    }
</script>

<style scoped>

</style>