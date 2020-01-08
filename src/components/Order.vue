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
              <h4>选择学生（输入姓名）按下tab键:</h4>
              <v-autocomplete
                v-model="student_id"
                :items="students"
                color="red"
                item-text="fullname"
                item-value="_id"
                label="学生姓名，fistname"
              ></v-autocomplete>
            </div>
            课程编号：{{ course_id }}<br>
            学生编号：{{ student_id }}
          </div>
          <div class="col-sm-6">
            <h3>一次性缴纳学费</h3>
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
      student_id:'',
      course_id:'',
      students:[],
      course: {
        _id:'',
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
      this.course_id = this.$route.params._id;
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
//      alert('selected student: ' + this.student_id);
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
              this.savePayment(chargeId);
              this.$router.push({ path: `/complete/${chargeId}` });
            })
            .catch((error) => {
              // eslint-disable-next-line
            alert('error send payload...' + error);
            });
        }
      });
    },
    savePayment(chargeId){
      const path = 'http://localhost:5000/payment';
      const payload = {
            chargeId: chargeId,
            courseId: this.course_id,
            studentId: this.student_id,
          };
      axios.post(path, payload)
        .then((res) => {
          console.log(res.data.message);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
  created() {
    const path = 'http://localhost:5000/students';
    axios.get(path)
      .then((res) => {
        this.students = res.data.students;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
      this.getCourse();
  },
};
</script>
