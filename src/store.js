import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    uid: undefined,
    user: {}, 
    order: {
      email: "",
      firstName: "",
      lastName: "",
      airport: "",
      userId: "",
      roomType: "",
      price: "",
      orderDate: "",
      stayDate: "",
      status: "",
      description: '',
      total:'',
    },
    course:{},
    orders: []
  },
  getters: {
    UID: state => {
      return state.uid;
    },
    USER: state => {
      return state.user;
    },
    ORDER: state => {
      return state.order;
    },
    ORDERS: state => {
      return state.orders;
    },
    COURSE: state => {
      return state.course;
    }
  },
  mutations: {
    SET_UID: (state, uid) => {
      state.uid = uid;
    },
    SET_USER: (state, user) => {
      // alert("Store:mutations:SET_USER:uid: " + user.uid);
      state.user = user;
    },
    SET_ORDER: (state, order) => {
      state.order = order;
    },
    SET_COURSE: (state, course) => {
      state.course = course
    }
  },
  actions: {
    SET_UID: (context, uid) => {
      context.commit("SET_UID", uid);
    },
    SET_USER: (context, user) => {
      // alert("Store:actions:SET_USER:user.uid: " + user.uid);
      context.commit("SET_USER", user);
    },
    SET_ORDER: (context, order) => {
      context.commit("SET_ORDER", order);
    },
    SET_COURSE: (context, course) => {
      context.commit("SET_COURSE", course);
    }
  }
});
