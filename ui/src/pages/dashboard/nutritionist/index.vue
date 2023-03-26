<template>
  <q-page class="flex flex-center">
      {{ results }}
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'IndexPage',
    data() {
        return {
            results: {},
        };
    },
    async created() {
        const response = await this.$api.get('/consultation/nutritionist', {
        });
        if (response.status === 200) {
            this.results = response.data;
        }
    },
});
</script>
