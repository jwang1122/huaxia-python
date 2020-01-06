import Vue from 'vue';
import Vuex from 'vuex';

Vue.component('v-select', VueSelect.VueSelect)

const store1 = new Vuex.Store({
  state: {
    people: [{
      "uuid": "58dc3c76c9205670b433e934",
      "email": "dennisingram@cinesanct.com"
    }, {
      "uuid": "58dc3c76fb733629909f1ce8",
      "email": "louhendricks@zytrac.com"
    }, {
      "uuid": "58dc3c762d5b19946660567e",
      "email": "cindyholcomb@tourmania.com"
    }],
    activePerson: null
  },
  mutations: {
    setActivePerson(state, person) {
      state.activePerson = person
    }
  }
})

new Vue({
    el: '#app',
    store1,
    methods:{
        setActivePersion(val){
            this.$store1.commit('setActivePerson', val)
        }
    },
    computed: {
        store1() {
            return this.$store1.state
        }
    }
})