# Huaxia development notes

## Back to main document
[Master ReadMe.md](../ReadMe.md)


## Install vuetify
```js
vue install --save @vue/cli
vue add vuetify
vue ui
```
非常重要，网上的vuetify的例子，比如v-autocomplete都是一半工作。
原因是在App.vue中必须使用<v-app>标记，而不是<div id="v-app">
···html
<template>
    <v-app>
        <div id="nav">
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link> | 
            <router-link v-if="authenticated" to="/activities"
            v-on:click.native="setAuthenticated(true)" replace>学校近期活动安排</router-link> | 
            <router-link v-if="authenticated" to="/courses">课程表</router-link> | 
            <router-link v-if="authenticated" to="/students">学生登记表</router-link> |
            <router-link to="/combo">Combobox test</router-link>
        </div>
        <router-view @authenticated="setAuthenticated" />
    </v-app>
</template>

···

## Avoid Unexpected console
```js
    // eslint-disable-next-line
    console.error(error);
```

## pass varialbe to python service
```js
      const path = `http://localhost:5000/files/${filename}`;
```
pay more attention on the sigle quatation mark, it is appasophy, 

## insert static html page to placeholder
Cannot use javascript FileReader() function to read the file. It is because, FileReader() reads file from client(user)'s machine, it is usually not allowed, must get user's permission, in other word, need use <input> field to let user choose file from the local file system, which is not what we want.
what we want is load static html page from server machine, and display it in placeholder.
1. create a python service to read file by give filename
```py
@app.route('/files/<filename>')
def readfile(filename):
    with open('../src/assets/' + filename) as f:
        text = f.read()

    response_object = {
        'status': 'success',
        'html': text
    }
    return jsonify(response_object), 200
``` 
2. Create a method in vue file
```js
    load() {
      const filename = 'grade1-3.html';
      alert(filename);
      const path = 'http://localhost:5000/files/grade1-3.html';
      axios.get(path)
        .then((res) => {
            alert(res.data.html);
          this.message = res.data.html;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
```
where the message is local variable defined in data(){return{message:""}} block.

3. in the template add
```html
    <div id="courseInfo">
      <span v-html="message"></span>
    </div>
```

## display image in assets
```html
<img src="@/assets/logo.png">
```
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