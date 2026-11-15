import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const TeaLeaf = () => import('@/views/tea_leaf/index.vue')
const TeaMaster = () => import('@/views/tea_master/index.vue')
const Disciple = () => import('@/views/disciple/index.vue')
const TeaSet = () => import('@/views/tea_set/index.vue')
const TeaMat = () => import('@/views/tea_mat/index.vue')
const DianCha = () => import('@/views/dian_cha/index.vue')
const TeaWater = () => import('@/views/tea_water/index.vue')
const TeaIncense = () => import('@/views/tea_incense/index.vue')
const TeaCeremony = () => import('@/views/tea_ceremony/index.vue')
const TeaPoetry = () => import('@/views/tea_poetry/index.vue')
const TeaBook = () => import('@/views/tea_book/index.vue')
const TeaRegion = () => import('@/views/tea_region/index.vue')
const TeaWorkshop = () => import('@/views/tea_workshop/index.vue')
const TeaContest = () => import('@/views/tea_contest/index.vue')
const TeaExchange = () => import('@/views/tea_exchange/index.vue')
const TeaMedia = () => import('@/views/tea_media/index.vue')
const TeaFund = () => import('@/views/tea_fund/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/tea_leaf', name: 'tea_leaf', component: TeaLeaf },
    { path: '/tea_master', name: 'tea_master', component: TeaMaster },
    { path: '/disciple', name: 'disciple', component: Disciple },
    { path: '/tea_set', name: 'tea_set', component: TeaSet },
    { path: '/tea_mat', name: 'tea_mat', component: TeaMat },
    { path: '/dian_cha', name: 'dian_cha', component: DianCha },
    { path: '/tea_water', name: 'tea_water', component: TeaWater },
    { path: '/tea_incense', name: 'tea_incense', component: TeaIncense },
    { path: '/tea_ceremony', name: 'tea_ceremony', component: TeaCeremony },
    { path: '/tea_poetry', name: 'tea_poetry', component: TeaPoetry },
    { path: '/tea_book', name: 'tea_book', component: TeaBook },
    { path: '/tea_region', name: 'tea_region', component: TeaRegion },
    { path: '/tea_workshop', name: 'tea_workshop', component: TeaWorkshop },
    { path: '/tea_contest', name: 'tea_contest', component: TeaContest },
    { path: '/tea_exchange', name: 'tea_exchange', component: TeaExchange },
    { path: '/tea_media', name: 'tea_media', component: TeaMedia },
    { path: '/tea_fund', name: 'tea_fund', component: TeaFund },
  ],
})

export default router
