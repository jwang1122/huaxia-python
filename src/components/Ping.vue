<template>
  <div class="container">
    <button type="button" class="btn btn-primary" @click="toggle()">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    toggle(){
      if(this.msg==='pong!') this.msg='ping!'
      else this.msg='pong!'
    }
  },
  created() {
    this.getMessage();
  },
};
</script>
