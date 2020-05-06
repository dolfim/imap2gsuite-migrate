import Vue from 'vue';
import VueRouter, { RouteConfig, Route } from 'vue-router';

import { getModule } from 'vuex-module-decorators';
import store from '@/store';
import Auth from '@/store/modules/auth';

import Login from '../views/Login.vue';
import Main from '../views/Main.vue';
import Task from '../views/Task.vue';

Vue.use(VueRouter);

const auth = getModule(Auth, store);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Main',
    component: Main,
    meta: {
      protected: true,
    },
  },
  {
    path: '/task/:taskId',
    name: 'Task',
    component: Task,
    meta: {
      protected: true,
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to: Route, from: Route, next: Function) => {
  if (to.matched.some((record) => record.meta.protected)) {
    if (auth.authenticated) {
      next();
    } else {
      next({
        name: 'Login',
        params: {
          nextUrl: to,
        },
      });
    }
  } else {
    next();
  }
});

// router.beforeEach((to, from, next) => {
//   store.dispatch('fetchAccessToken');
//   if (to.fullPath === '/users') {
//     if (!store.state.accessToken) {
//       next('/login');
//     }
//   }
//   if (to.fullPath === '/login') {
//     if (store.state.accessToken) {
//       next('/users');
//     }
//   }
//   next();
// });

export default router;
