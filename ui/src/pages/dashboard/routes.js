export default [
    { path: 'nutritionist', name: 'nutritionist-home', component: () => import('pages/dashboard/nutritionist/index.vue') },
    { path: 'patient', name: 'patient-home', component: () => import('pages/dashboard/patient/index.vue') },
];
