export default [
    { path: 'meals/new', name: 'create-meal', component: () => import('pages/meal_plan/meal/create/index.vue') },
    { path: 'meals', name: 'list-meals', component: () => import('pages/meal_plan/meal/list/index.vue') },
    { path: 'meals/patients', name: 'list-patients-meals', component: () => import('pages/meal_plan/meal/review/index.vue') },
];
