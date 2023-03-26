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
            ],
        };
    },
    computed: {
        ...mapState(useLoginStore, ['userInfo']),
    },
    methods: {
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
