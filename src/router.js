import Vue from 'vue';
import Router from 'vue-router';
import ClassesComponent from './components/Classes.vue';
import Order from './components/Order.vue';
import Ping from './components/Ping.vue';
import OrderComplete from './components/OrderComplete.vue';
import LoginComponent from '@/views/login.vue';
import SecureComponent from '@/views/secure.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: {
        name: "login"
      }
    },
    {
      path: "/login",
      name: "login",
      component: LoginComponent
    },
    {
      path: "/secure",
      name: "secure",
      component: SecureComponent
    },
    {
      path: '/classes',
      name: 'classes',
      component: ClassesComponent,
    },
    {
      path: '/order/:_id',
      name: 'Order',
      component: Order,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/complete/:id',
      name: 'OrderComplete',
      component: OrderComplete,
    },
  ],
});
