<template>
    <q-page class="list-patient-meals-page">
        <div class="row justify-between q-pb-lg">
            <div class="text-h4">My meals</div>
            <q-btn :to="{name: 'create-meal'}" color="blue" label="New Meal"/>
        </div>
        <div class="meals-list">
            <q-list>
                <q-item v-for="(meal, index) in meals" :key="index">
                    <q-card>
                        <q-card-section>
                            <div class="text-h6">Posted on: {{ meal.time_created }}</div>
                            <div class="row no-wrap justify-between">
                                <div class="column q-pr-md">
                                    <div class="row items-baseline" v-if="meal.planned_meal.name">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Name:
                                        </div>
                                        {{ meal.planned_meal.name }}
                                    </div>
                                    <div class="row items-baseline">
                                        <div class="q-pr-xs text-body1 text-weight-bold">
                                            Type:
                                        </div>
                                        {{ mealTypes[meal.planned_meal.meal_type] }}
                                    </div>
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
                    </q-card>
                </q-item>
            </q-list>
        </div>
    </q-page>
</template>
<script>
export default {
    name: 'list-patient-meals',
    data() {
        return {
            meals: [],
            mealStatuses: {
                approved: 'Approved',
                rejected: 'Rejected',
                pending_review: 'Pending Review',
            },
            mealTypes: {
                breakfast: 'Breakfast',
                morning_snack: 'Morning Snack',
                lunch: 'Lunch',
                afternoon_snack: 'Afternoon Snack',
                dinner: 'Dinner',
            },
        };
    },
    async created() {
        const response = await this.$api.get('meals');
        if (response.status === 200) {
            this.meals = response.data;
        }
    },
};
</script>
<style lang="scss">
.list-patient-meals-page {
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
