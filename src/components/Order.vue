<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>确定要注册了吗?</h1>
        <hr>
        <router-link to="/courses" class="btn btn-primary">
          返回
        </router-link>
        <br><br><br>

        <div class="row">
          <div class="col-sm-6">
            <div>
              <h4>您所注册的课程:</h4>
              <ul>
                <li>课程名称: <em>{{ course.title }} / {{course.teacher}}</em></li>
                <li>学期学费: <em>${{ course.price }}</em></li>
              </ul>
            </div>

            <div>
              <h4>Use this info for testing:</h4>
      <v-autocomplete
         :items="students"
        color="red"
        item-text="fullname"
        label="Student"
      ></v-autocomplete>
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
      student:{},
      students:[],
      course: {
        title: '',
        teacher: '',
        classroom: '',
        infolink:'',
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
    getCourse() {
      const path = `http://localhost:5000/courses/${this.$route.params._id}`;
      axios.get(path)
        .then((res) => {
          this.course = res.data.course;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    validate() {
//      alert('validate()...');
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
          console.log("@JWANG: " + this.course['price']);
          const payload = {
            course: this.course,
            token: response.id,
          };
          const path = 'http://localhost:5000/charge';
          axios.post(path, payload)
            .then((res) => {
              let chargeId = res.data.charge.id;
              this.$router.push({ path: `/complete/${chargeId}` });
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
    this.students=[
      {"fullname":"john wang","_id":"12345"},
      {"fullname":"ailian wang","_id":"34562"},
      {"fullname":"charlse wang","_id":"11111"},
      {"fullname":"weiping xing","_id":"22222"},
      {"fullname":"jun wu","_id":"56423"},
      {"fullname":"helen yang","_id":"97543"},
    ];
    this.getCourse();
  },
};
</script>
