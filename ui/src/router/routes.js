const routes = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            { path: 'nutritionist', name: 'nutritionist-home', component: () => import('pages/IndexPage.vue') },
            { path: 'patient', name: 'patient-home', component: () => import('pages/IndexPage.vue') },
        ],
    },
    {
        path: '/login',
        component: () => import('layouts/CleanLayout.vue'),
        children: [
            { name: 'login', path: '', component: () => import('pages/Login.vue') },
        ],
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () => import('pages/ErrorNotFound.vue'),
    },
];

export default routes;
