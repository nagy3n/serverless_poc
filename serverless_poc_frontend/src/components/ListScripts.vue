<template>
    <v-data-table
            :headers="headers"
            :items="scripts"
            :items-per-page="5"
            class="elevation-1"
    >
<!--        <template v-slot:item.calories="{ item }">-->
<!--          <v-chip :color="getColor(item.calories)" dark>{{ item.calories }}</v-chip>-->
<!--        </template>-->
    </v-data-table>
</template>

<script>
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
        })
    }
</script>

<style scoped>

</style>