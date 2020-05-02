<template>
    <v-card>
        <v-card-title>Add a script</v-card-title>
        <v-card-text>
            <v-form v-model="valid">
                <v-file-input :rules="[value => !!value || 'Required']" accept=".py" label="Script File"
                              v-model="scriptFile"></v-file-input>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn :disabled="!valid" @click="submitScript()">Submit</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import {HTTP} from "../utils";

    export default {
        name: "AddScript",
        data: () => ({
            valid: null,
            scriptFile: null
        }),
        methods: {
            submitScript(){
                let formData = new FormData();
                formData.append("script", this.scriptFile);
                HTTP.post('/upload/', formData).then(() => this.$router.push({name: "list-scripts"}))
            }
        }
    }
</script>

<style scoped>

</style>