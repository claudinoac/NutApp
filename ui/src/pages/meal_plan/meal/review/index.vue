<template>
    <q-page class="review-meals-page">
        <div class="row justify-between q-pb-lg">
            <div class="text-h4">Patients meals</div>
            <search-field v-model="search" placeholder="Search user meals"/>
        </div>
        <div class="meals-list">
            <q-list v-if="meals.length > 0">
                <q-item v-for="(meal, index) in meals" :key="index">
                    <q-card>
                        <q-card-section>
                            <div class="text-h6">
                                Posted on: {{ meal.time_created }} by {{ meal.patient.name }}
                            </div>
                            <div class="row no-wrap justify-between">
                                <div class="column q-pr-md">
                                    <template v-if="meal.items.length > 0">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Items:
                                        </div>
                                        <div
                                            v-for="(item, idx) in meal.items"
                                            :key="idx" class="q-pl-md"
                                        >
                                            - <b class="q-pr-xs">{{ item.name }}:</b>
                                            {{ item.quantity }}
                                        </div>
                                    </template>
                                    <template v-if="meal.planned_meal.items.length > 0">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Planned Items:
                                        </div>
                                        <div
                                            v-for="(item, idx) in meal.planned_meal.items"
                                            :key="idx" class="q-pl-md"
                                        >
                                            - <b class="q-pr-xs">{{ item.name }}:</b>
                                            {{ item.quantity }}
                                        </div>
                                    </template>
                                    <div class="row items-baseline">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Review status:
                                        </div>
                                        {{ mealStatuses[meal.status] }}
                                    </div>
                                    <div class="column" v-if="meal.feedback">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Feedback:
                                        </div>
                                        <div class="q-pl-md">
                                            - {{ meal.feedback}}
                                        </div>
                                    </div>
                                </div>
                                <img
                                    v-if="meal.photo" width="300" height="300"
                                    :src="`http://localhost:7200/media/${meal.photo}`"
                                />
                            </div>
                        </q-card-section>
                        <q-card-actions v-if="meal.status === 'pending_review'" class="justify-end">
                            <q-btn
                                color="red" label="reject" @click="reviewMeal(meal.id, 'rejected')"
                            />
                            <q-btn
                                color="positive" label="approve"
                                @click="reviewMeal(meal.id, 'approved')"
                            />
                        </q-card-actions>
                    </q-card>
                </q-item>
            </q-list>
            <q-card v-else>
                <q-card-section>
                    No matching records.
                </q-card-section>
            </q-card>
        </div>
    </q-page>
</template>
<script>
import SearchField from 'src/components/search.vue';

export default {
    name: 'list-patients-meals',
    components: {
        SearchField,
    },
    data() {
        return {
            meals: [],
            mealStatuses: {
                approved: 'Approved',
                rejected: 'Rejected',
                pending_review: 'Pending Review',
            },
            search: '',
        };
    },
    created() {
        this.loadData();
    },
    watch: {
        search() {
            this.loadData(this.search);
        },
    },
    methods: {
        async loadData(searchData) {
            const response = await this.$api.get('meals/patients', { params: { q: searchData } });
            if (response.status === 200) {
                this.meals = response.data;
            }
        },
        async reviewMeal(mealId, value) {
            const promptName = value === 'approved' ? 'Approve' : 'Reject';
            this.$q.dialog({
                title: `${promptName} meal`,
                message: 'Write a comment about this meal to the patient',
                prompt: {
                    model: '',
                    type: 'textarea',
                },
                cancel: true,
                persistent: true,
            }).onOk(async (comment) => {
                const response = await this.$api.put(`meal/${mealId}/feedback`, {
                    feedback: comment,
                    status: value,
                });
                if (response.status === 200) {
                    this.$q.notify({
                        message: 'Review successfully submitted.',
                        type: 'positive',
                    });
                    this.loadData();
                }
            });
        },
    },
};
</script>
<style lang="scss">
.review-meals-page {
    padding: 40px;

    .meals-list {
        max-width: 800px;

        .q-card {
            min-width: 500px;
            width: 100%;
        }
    }
}
</style>
