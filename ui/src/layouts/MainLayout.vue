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

        <div>Logout</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
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
        };
    },
    computed: {
        ...mapState(useLoginStore, ['userInfo']),
    },
    methods: {
        toggleLeftDrawer() {
            this.leftDrawerOpen = !this.leftDrawerOpen;
        },
    },
});
</script>
