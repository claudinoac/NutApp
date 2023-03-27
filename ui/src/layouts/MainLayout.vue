<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-blue-5">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
            Hi, {{ userInfo.first_name }} {{ userInfo.last_name }}
        </q-toolbar-title>
        <div v-if="patientData" class="row items-center">
            <div class="q-pr-md row">
                <div class="q-px-sm">
                    <b class="q-pr-xs">Current score:</b> {{ patientData.accumulated_score }}
                </div>
            </div>
            <div class="q-pr-md row">
                <div class="q-px-sm">
                    <b class="q-pr-xs">Streak score:</b> {{ patientData.streak_score }}
                </div>
            </div>
        </div>

        <a href="#" @click="logout" style="text-decoration: none; color: white">Logout</a>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <template  v-for="(link, idx) in links" :key="idx">
            <q-item
                clickable
                :to="link.to"
                v-if="link.isAllowed(userInfo.account_type)"
                v-ripple
            >
                <q-item-section>
                    <div class="text-body1">{{ link.label }}</div>
                </q-item-section>
            </q-item>
        </template>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { mapState } from 'pinia';
import { defineComponent } from 'vue';
import { useLoginStore } from 'src/stores/login';

export default defineComponent({
    name: 'MainLayout',
    data() {
        return {
            leftDrawerOpen: true,
            links: [
                { to: { name: 'list-meals' }, isAllowed: (accountType) => accountType === 'patient', label: 'My Meals' },
                { to: { name: 'create-meal' }, isAllowed: (accountType) => accountType === 'patient', label: 'New Meal' },
                { to: { name: 'list-patients' }, isAllowed: (accountType) => accountType === 'nutritionist', label: 'My Patients' },
                {
                    to: { name: 'list-patients-meals' },
                    isAllowed: (accountType) => accountType === 'nutritionist',
                    label: 'Patients Meals',
                },
            ],
            patientData: null,
        };
    },
    computed: {
        ...mapState(useLoginStore, ['userInfo']),
    },
    watch: {
        userInfo: {
            deep: true,
            immediate: true,
            handler() {
                this.getPatientInfo();
            },
        },
    },
    methods: {
        async getPatientInfo() {
            if (this.userInfo.account_type === 'patient') {
                const response = await this.$api.get('patient/profile');
                if (response.status === 200) {
                    this.patientData = response.data;
                }
            }
        },
        toggleLeftDrawer() {
            this.leftDrawerOpen = !this.leftDrawerOpen;
        },
        async logout() {
            await this.$api.get('login/logout');
            this.$router.push({ name: 'login' });
        },
    },
});
</script>
