import Vue from 'vue';
import Router from 'vue-router';
import CoursesComponent from './components/Courses.vue';
import ActivitiesComponent from '@/views/activities.vue';
import Order from './components/Order.vue';
import Ping from './components/Ping.vue';
import OrderComplete from './components/OrderComplete.vue';
import LoginComponent from '@/views/login.vue';
import SecureComponent from '@/views/secure.vue';
import StudentsComponent from "@/components/Students.vue";

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
      path: "/activities",
      name: "activities",
      component: ActivitiesComponent
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesComponent,
    },
    {
      path: '/students',
      name: 'students',
      component: StudentsComponent,
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
