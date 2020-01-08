<template>
  <div id="login" >
    <h1>Login</h1>
    <input type="text" class="form-control" name="username" v-model="input.username" placeholder="Username" required/><br>
    <input type="password" class="form-control" name="password" v-model="input.password" placeholder="Password" required/><br>
    <button type="button" class="btn btn-primary" v-on:click="login()">登录</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Login",
  user: {},
  data() {
    return {
      input: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      if (this.input.username != "" && this.input.password != "") {
        this.authenticate(this.input.username, this.input.password);
      } else {
        alert("A username and password must be present.");
      }
    },
    authenticate(username, password){
      const path = `http://localhost:5000/users/${username}`;
      axios.get(path)
        .then((res) => {
          this.user = res.data.user;
//          alert("@JWANG: " + this.user['email'] + '/' + password);
          if(password==this.user['password']){
            this.$emit("authenticated", true);
            this.$emit("user", this.user);
            this.$store.commit("SET_USER", this.user);
            this.$router.replace({ name: "courses" });
          } else {
            alert("The username and / or password is incorrect");
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

    }
  }
};
</script>

<style scoped>
#login {
  width: 400px;
  border: 1px solid #cccccc;
  background-color: lightblue;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
</style>