import DashboardRoutes from 'src/pages/dashboard/routes';
import MealPlanRoutes from 'src/pages/meal_plan/routes';
import PatientRoutes from 'src/pages/patient/routes';

const routes = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            ...DashboardRoutes,
            ...MealPlanRoutes,
            ...PatientRoutes,
        ],
    },
    {
        path: '/login',
        component: () => import('layouts/CleanLayout.vue'),
        children: [
            { name: 'login', path: '', component: () => import('pages/login/index.vue') },
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
