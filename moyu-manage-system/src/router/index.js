import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/dashboard'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '系统首页' }
                },
                {
                    path: '/table',
                    component: () => import(/* webpackChunkName: "table" */ '../components/page/BaseTable.vue'),
                    meta: { title: '住户信息' }
                },
                {
                    path: '/tabs',
                    component: () => import(/* webpackChunkName: "tabs" */ '../components/page/Tabs.vue'),
                    meta: { title: '系统信息' }
                },
                {
                    path: '/form_1',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/NavigationForm.vue'),
                    meta: { title: '导航功能' }
                },
                {
                    path: '/form_2',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/DeliverForm.vue'),
                    meta: { title: '送物功能' }
                },
                {
                    path: '/form_3',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/MoveCtrlForm.vue'),
                    meta: { title: '人工控制' }
                },
                {
                    path: '/form_4',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/MappingForm.vue'),
                    meta: { title: '建图功能' }
                },
                {
                    path: '/form_5',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/VoiceRegForm.vue'),
                    meta: { title: '语音识别' }
                },
                {
                    // 团队信息介绍
                    path: '/i18n',
                    component: () => import(/* webpackChunkName: "i18n" */ '../components/page/I18n.vue'),
                    meta: { title: '作者团队信息' }
                },
                {
                    // 权限页面
                    path: '/permission',
                    component: () => import(/* webpackChunkName: "permission" */ '../components/page/Permission.vue'),
                    meta: { title: '权限测试', permission: true }
                },
                {
                    path: '/403',
                    component: () => import(/* webpackChunkName: "403" */ '../components/page/403.vue'),
                    meta: { title: '403' }
                },
            ]
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Login.vue'),
            meta: { title: '登录' }
        },
        {
            path: '*',
            redirect: '/404'
        }
    ]
});
