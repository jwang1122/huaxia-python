# Huaxia development notes

## use store to save the shared data cross the application
1. add store.js into src folder;
2. add the following store related lines in main.js
```js
import store from "./store";
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
```
3. To save user information to store
```js
this.$store.commit("SET_USER", this.user);
```

4. To get user information from store
```js
this.user = this.$store.getters.USER;
```