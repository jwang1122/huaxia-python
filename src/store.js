import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    uid: undefined,
    roomId: undefined,
    user: {}, // firebase author user
    profile: {
      id: "",
      user: {},
      firstName: "",
      lastName: "",
      email: ""
    },
    product: {
      roomType: "",
      price: ""
    },
    products: [],
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
    orders: []
  },
  getters: {
    UID: state => {
      return state.uid;
    },
    ROOMID: state => {
      return state.roomId;
    },
    USER: state => {
      return state.user;
    },
    PROFILE: state => {
      return state.profile;
    },
    PRODUCT: state => {
      return state.product;
    },
    PRODUCTS: state => {
      return state.products;
    },
    ORDER: state => {
      return state.order;
    },
    ORDERS: state => {
      return state.orders;
    }
  },
  mutations: {
    SET_UID: (state, uid) => {
      state.uid = uid;
    },
    SET_ROOMID: (state, roomId) => {
      // alert("Store:mutations:SET_ROOMID:roomid: " + roomId);
      state.roomId = roomId;
    },
    SET_USER: (state, user) => {
      // alert("Store:mutations:SET_USER:uid: " + user.uid);
      state.user = user;
    },
    SET_PROFILE: (state, profile) => {
      state.profile = profile;
    },
    SET_PRODUCT: (state, product) => {
      state.product = product;
    },
    SET_ORDER: (state, order) => {
      state.order = order;
    }
  },
  actions: {
    SET_UID: (context, uid) => {
      context.commit("SET_UID", uid);
    },
    SET_ROOMID: (context, roomId) => {
      context.commit("SET_ROOMID", roomId);
    },
    SET_USER: (context, user) => {
      // alert("Store:actions:SET_USER:user.uid: " + user.uid);
      context.commit("SET_USER", user);
    },
    SET_ORDER: (context, order) => {
      context.commit("SET_ORDER", order);
    },
    SET_PRODUCT: (context, product) => {
      context.commit("SET_PRODUCT", product);
    }
  }
});
