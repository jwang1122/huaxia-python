<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Ready to buy?</h1>
        <hr>
        <router-link to="/" class="btn btn-primary">
          Back Home
        </router-link>
        <br><br><br>
        <div class="row">
          <div class="col-sm-6">
            <div>
              <h4>You are buying:</h4>
              <ul>
                <li>class Title: <em>{{ class0.title }} / {{class0.teacher}}</em></li>
                <li>Amount: <em>{{ class0.price }}</em></li>
              </ul>
            </div>
            <div>
              <h4>Use this info for testing:</h4>
              <ul>
                <li>Card Number: 4242424242424242</li>
                <li>CVC Code: any three digits</li>
                <li>Expiration: any date in the future</li>
              </ul>
            </div>
          </div>
          <div class="col-sm-6">
            <h3>One time payment</h3>
            <br>
            <form>
              <div class="form-group">
                <label>Credit Card Info</label>
                <input type="text"
                       class="form-control"
                       placeholder="XXXXXXXXXXXXXXXX"
                       v-model = "card.number"
                       required>
              </div>
              <div class="form-group">
                <input type="text"
                       class="form-control"
                       placeholder="CVC"
                       v-model = "card.cvc"
                       required>
              </div>
              <div class="form-group">
                <label>Card Expiration Date</label>
                <input type="text"
                       class="form-control"
                       placeholder="MM/YY"
                       v-model = "card.exp"
                       required>
              </div>
              <div v-show="errors">
                    <br>
                    <ol class="text-danger">
                        <li v-for="(error, index) in errors" :key="index">
                        {{ error }}
                        </li>
                    </ol>
                </div>
              <button class="btn btn-primary btn-block"
                @click.prevent="validate" :disabled="stripeCheck">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="https://js.stripe.com/v2/"></script>
<script>
import axios from 'axios';
import stripeKey from '@/config.js'

export default {
  data() {
    return {
      class0: {
        title: '',
        teacher: '',
        classroom: '',
        price: 0,
      },
      card: {
        number: '',
        cvc: '',
        exp: '',
      },
      errors: [],
      stripePublishableKey: stripeKey.STRIPE_PUBLIC_KEY,
      stripeCheck: false,
    };
  },
  methods: {
    getClass() {
      const path = `http://localhost:5000/classes/${this.$route.params._id}`;
      axios.get(path)
        .then((res) => {
          this.class0 = res.data.class0;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    validate() {
      alert('validate()...');
      this.errors = [];
      let valid = true;
      if (!this.card.number) {
        valid = false;
        this.errors.push('Card Number is required');
      }
      if (!this.card.cvc) {
        valid = false;
        this.errors.push('CVC is required');
      }
      if (!this.card.exp) {
        valid = false;
        this.errors.push('Expiration date is required');
      }
      if (valid) {
        this.createToken();
      }
    },
    createToken() {
      this.stripeCheck = true;
      window.Stripe.setPublishableKey(this.stripePublishableKey);
      window.Stripe.createToken(this.card, (status, response) => {
//        alert(`status: ${status}`);
        if (response.error) {
          this.stripeCheck = false;
          this.errors.push(response.error.message);
          // eslint-disable-next-line
        } else {
          console.log("@JWANG: " + this.class0['price']);
          const payload = {
            class0: this.class0,
            token: response.id,
          };
          const path = 'http://localhost:5000/charge';
          axios.post(path, payload)
            .then((res) => {
              this.$router.push({ path: `/complete/${res.data.charge.id}` });
            })
            .catch((error) => {
              // eslint-disable-next-line
            alert('error send payload...' + error);
            });
        }
      });
    },

  },
  created() {
    this.getClass();
  },
};
</script>
