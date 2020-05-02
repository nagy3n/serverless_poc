<template>
    <div>
        <v-card>
            <v-card-title>Arguments</v-card-title>
            <v-card-text>
                <v-form v-model="valid">
                    <v-layout wrap>
                        <v-flex v-for="(argument, argumentIndex) in script_arguments" :key="argumentIndex" class="pa-3"
                                xs6>
                            <v-text-field v-model="filled_arguments[argument]"
                                          :rules="[value => !!value || 'Required']" :label="argument"></v-text-field>
                        </v-flex>
                    </v-layout>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled="!valid" @click="submitScript()">Submit</v-btn>
            </v-card-actions>
        </v-card>
        <v-card v-if="result" class="mt-4">
            <v-card-title>Result</v-card-title>
            <v-card-text>
                {{result}}
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
    import {HTTP} from "../utils";

    export default {
        name: "ExecuteScript",
        created() {
            HTTP.get(`/get_script_arguments/${this.$route.params.scriptName}`).then(res => this.script_arguments = res.data)
        },
        data: () => ({
            script_arguments: [],
            filled_arguments: {},
            result: null,
            valid: null
        }),
        methods: {
            submitScript() {
                let formData = new FormData();
                formData.append("script", this.scriptFile);
                HTTP.post(`/run_script/${this.$route.params.scriptName}`, this.filled_arguments).then(res => this.result = res.data)
            }
        }
    }
</script>

<style scoped>

</style>