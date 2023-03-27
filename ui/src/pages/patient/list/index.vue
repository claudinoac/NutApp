<template>
    <q-page class="list-patients">
        <div class="row justify-between q-pb-lg">
            <div class="text-h4">My Patients</div>
        </div>
        <q-table :rows="patients" :columns="columns"/>
    </q-page>
</template>
<script>
export default {
    name: 'list-patients',
    data() {
        return {
            patients: [],
            columns: [
                { field: 'name', label: 'Name', align: 'left' },
                { field: 'accumulated_score', label: 'Accumulated Score', align: 'center' },
                { field: 'streak_score', label: 'Streak Score', align: 'center' },
                { field: 'available_days_off', label: 'Available Days Off', align: 'center' },
            ],
        };
    },
    async created() {
        const response = await this.$api.get('patients');
        if (response.status === 200) {
            this.patients = response.data;
        }
    },
};
</script>
<style lang="scss">
.list-patients {
    padding: 40px;
}
</style>
