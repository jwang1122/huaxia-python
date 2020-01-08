<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>衷心感谢您注册中文学校的学习课程!</h1>
        <h2>课程名称: {{ this.course.description }}</h2>
        <h2>学期学费: ${{ this.course.amount }}</h2>
        <h2>缴费确认编号：{{ this.chargeId }}</h2>
        <hr><br>
        <router-link to="/courses" class="btn btn-primary btn-sm">返回</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      chargeId:'',
      course: {
        description: '',
        amount: 0,
      },
    };
  },
  methods: {
    getChargeInfo() {
      this.chargeId = this.$route.params.id;
      const path = `http://localhost:5000/charge/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.course.description = res.data.charge.description;
          this.course.amount = res.data.charge.amount;
          this.course.amount = this.course.amount / 100;
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
