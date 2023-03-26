import { boot } from 'quasar/wrappers';
import axios from 'axios';

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
import { Notify } from 'quasar';

const api = axios.create({
    baseURL: '/api',
    headers: {
        'X-Requested-With': 'axios',
    },
});

api.interceptors.response.use(
    (response) => {
        const message = response.data?.detail;
        if (message) {
            Notify.create({
                type: 'positive',
                message,
            });
        }
        return response;
    },
    async (error) => {
        if (
            (
                error.response
                && (error.response.status > 400 && error.response.status !== 404)
            )
            || (!error.response.config.ignore400 && error.response.status === 400)
        ) {
            const responseData = error.response.data;
            const message = responseData.detail
                || responseData.error
                || 'Something went wrong. Please try again later.';
            Notify.create({
                type: 'negative',
                message,
            });
        }
        return error?.response || {};
    },
);

export default boot(({ app }) => {
    // for use inside Vue files (Options API) through this.$axios and this.$api

    app.config.globalProperties.$axios = axios;
    // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
    //       so you won't necessarily have to import axios in each vue file

    app.config.globalProperties.$api = api;
    // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
    //       so you can easily perform requests against your app's API
});

export { api };
