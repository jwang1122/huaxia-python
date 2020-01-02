# Huaxia development notes

## use constants for stripe publishable key and secret key
in any vue file which use these keys add following import
```js
import stripeKey from '@/config.js'
```
where the config.js file will not save to GitHub for security reason

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