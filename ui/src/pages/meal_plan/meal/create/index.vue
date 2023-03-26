<template>
    <q-page class="new-meal-page">
        <div class="text-h4 q-pb-lg">New Meal</div>
        <q-form @submit.prevent="submitForm">
            <div class="column q-pb-md">
                <b>Choose a planned meal:</b>
                <q-select
                    v-model="plannedMeal"
                    :options="plannedMeals"
                    :rules="[val => !!val || 'This field is required']"
                    option-label="name"
                    outlined dense options-dense
                />
            </div>
            <q-card v-if="plannedMeal" class="q-mb-md">
                <q-card-section>
                    <div class="text-h6">{{ plannedMeal.name || mealType }}</div>
                    <div class="text-subtitle2" v-if="plannedMeal.name">
                        {{ mealType }}
                    </div>
                </q-card-section>
                <q-separator dark inset />

                <q-card-section class="q-pt-none">
                    <q-list>
                        <q-item-label
                            v-for="(item, index) in plannedMeal.items" :key="index"
                        >
                        <b>{{ item.name }}</b>: {{ item.quantity }}
                        </q-item-label>
                    </q-list>
                </q-card-section>
            </q-card>
            <div class="column q-pb-md">
                <b class="q-pb-xs">Date:</b>
                <date-picker v-model="form.date"/>
            </div>
            <div class="column q-pb-md">
                <b class="q-pb-xs">Hour:</b>
                <hour-picker v-model="form.hour"/>
            </div>
            <div class="column q-pb-md">
                <div class="row justify-between items-center">
                    <b class="text-h6">Items:</b>
                    <q-btn @click="addItem" label="Add Item" color="blue" no-caps/>
                </div>
                <q-list dense padding tag="ul">
                    <q-item v-for="(item, idx) in form.items" :key="idx" class="meal-item">
                        <q-item-section>
                            <div class="flex row items-center no-wrap q-pb-xs">
                                <q-input
                                    :rules="[val => !!val || 'This field is required']"
                                    outlined dense v-model="form.items[idx].name"
                                    class="q-pr-xs" style="width: 224px"
                                    label="Item name"
                                /><b style="padding-bottom: 20px">:</b>
                                <q-input
                                    :rules="[val => !!val || 'This field is required']"
                                    class="q-px-md" label="Item quantity"
                                    outlined dense v-model="form.items[idx].quantity"
                                />
                                <q-icon
                                    color="red" @click="form.items.splice(idx,1)"
                                    name="mdi-delete" size="23px" style="padding-bottom: 20px"
                                />
                            </div>
                        </q-item-section>
                    </q-item>
                </q-list>
            </div>
            <q-file
                clearable bottom-slots outlined dense
                v-model="model" label="Attach Photo" counter
                accept=".jpg, .png"
                @update:modelValue="previewImage"
            >
                <template v-slot:append>
                    <q-icon name="attach_file" />
                </template>
            </q-file>
            <div class="flex justify-end q-pt-md">
                <q-btn type="submit" label="Submit" color="green-9"/>
            </div>
        </q-form>
    </q-page>
</template>
<script>
import DatePicker from 'src/components/datepicker.vue';
import HourPicker from 'src/components/hourpicker.vue';

export default {
    name: 'create-meal',
    components: {
        DatePicker,
        HourPicker,
    },
    data() {
        return {
            plannedMeals: [],
            plannedMeal: null,
            form: {
                items: [],
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
    computed: {
        mealType() {
            return this.mealTypes[this.plannedMeal.meal_type];
        },
    },
    async created() {
        const response = await this.$api.get('meal_plan/patient');
        if (response.status === 200) {
            this.plannedMeals = response.data.meals;
        }
        const date = new Date();
        this.form.date = date.toLocaleDateString('pt-BR', { // you can use undefined as first argument
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
        });
        let hours = parseInt(date.getHours(), 10);
        hours = (`0${hours}`).slice(-2);
        const minutes = (`0${date.getMinutes()}`).slice(-2);
        this.form.hour = `${hours}:${minutes}`;
    },
    methods: {
        addItem() {
            this.form.items.push({});
        },
        previewImage(file) {
            console.log(file);
        },
        async submitForm() {
            if (this.form.items < 1) {
                this.$q.notify({
                    type: 'negative', message: 'Include at least an item to this meal.',
                });
                return;
            }
            const response = await this.$api.post('meals', {
                ...this.form,
                planned_meal: this.plannedMeal.id,
            });
            if (response.status === 201) {
                this.$q.notify({ message: 'Meal successfully submitted.', type: 'positive' });
                this.$router.push({ name: 'list-meals' });
            }
        },
    },
};
</script>
<style lang="scss">
.new-meal-page {
    padding: 40px;

    .q-form {
        max-width: 400px;
    }

    .meal-item {
        padding: 2px 0;
    }
}
</style>
