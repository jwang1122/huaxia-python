<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Thanks for purchasing!</h1>
        <h2>Book Name: {{ this.book.description }}</h2>
        <h2>Total Amount: ${{ this.book.amount }}</h2>
        <hr><br>
        <router-link to="/" class="btn btn-primary btn-sm">Back Home</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {
        description: '',
        amount: 0,
      },
    };
  },
  methods: {
    getChargeInfo() {
      const path = `http://localhost:5000/charge/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.book.description = res.data.charge.description;
          this.book.amount = res.data.charge.amount;
          this.book.amount = this.book.amount / 100;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getChargeInfo();
  },
};
</script>
