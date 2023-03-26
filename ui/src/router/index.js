import { Loading } from 'quasar';
import { createRouter, createWebHistory } from 'vue-router';
import { api } from 'boot/axios';
import routes from './routes';
import { useLoginStore } from '../stores/login';

const router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,
    history: createWebHistory(process.env.VUE_ROUTER_BASE),
});

router.beforeEach(async (to, from, next) => {  // eslint-disable-line
    const loginStore = useLoginStore();
    Loading.show({ message: 'Loading page...' });
    if (to.name !== 'login') {
        const response = await api.get('login/me');
        if (response.status === 200 && response.data?.is_active) {
            const userInfo = Object.freeze(response.data);
            loginStore.updateUserInfo(userInfo);
        } else {
            return next({ name: 'login', query: { next: to.path } });
        }
    }
    await Loading.hide();
    next();
});

export default router;
