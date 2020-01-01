import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books.vue';
import Classes from './components/Classes.vue';
import Order from './components/Order.vue';
import Ping from './components/Ping.vue';
import OrderComplete from './components/OrderComplete.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/Books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/',
      name: 'Classes',
      component: Classes,
    },
    {
      path: '/order/:id',
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
