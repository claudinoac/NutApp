<template>
    <q-page class="login-page">
        <q-form @submit.prevent="submitForm" class="q-pa-lg">
            <q-card>
                <q-card-section>
                    <div class="text-h6">NutApp - Login</div>
                </q-card-section>

                <q-card-section>
                    <q-input
                        outlined dense label="email"
                         v-model="form.email" class="q-mb-md"
                        :rules="[validateEmail]"
                    />
                    <q-input
                        type="password"
                        outlined dense label="password" v-model="form.password"
                        :rules="[(val) => !!val || 'This field is required.']"
                    />
                </q-card-section>
                <q-card-actions>
                    <q-btn
                        class="q-pt-md full-width"
                        color="light-blue-4" type="Login" label="Submit"
                    />
                </q-card-actions>
            </q-card>
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
            const response = await this.$api.post('/login/', this.form);
            if (response.status === 200 && response.data.is_active) {
                await this.$q.notify({ message: 'Login Successful', type: 'positive' });
                if (this.$route.query.next) {
                    this.$router.push(this.$route.query.next);
                } else if (response.data.account_type === 'nutritionist') {
                    this.$router.push({ name: 'nutritionist-home' });
                } else {
                    this.$router.push({ name: 'patient-home' });
                }
            }
        },
        validateEmail(value, rules) {
            return rules.email(value) || 'Please enter a valid email address';
        },
    },
};
</script>
<style lang="scss">
.login-page {
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url('login-background.jpg');
    background-repeat: no-repeat;
    background-size: cover;

    .q-form {
        min-width: 400px;
        max-width: 600px;
        min-height: 40%;
    }
}
</style>
