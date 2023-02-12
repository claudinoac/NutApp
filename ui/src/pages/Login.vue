<template>
    <q-page>
        <q-form @submit.prevent="submitForm" class="q-pa-lg">
            <q-input label="email" v-model="form.email"/>
            <q-input label="password" v-model="form.password"/>
            <q-btn class="q-pt-md" type="submit" label="Submit"/>
        </q-form>
    </q-page>
</template>
<script>
export default {
    name: 'LoginView',
    data() {
        return {
            form: {
                email: '',
                password: '',
            },
        };
    },
    methods: {
        async submitForm() {
            try {
                await this.$api.post('/login', this.form);
                return this.$q.notify({ message: 'Login Successful', type: 'positive' });
            } catch (e) {
                return this.$q.notify({ message: e.response.data.detail, type: 'negative' });
            }
        },
    },
};
</script>
