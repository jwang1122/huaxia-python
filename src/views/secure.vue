<template>
  <div id="secure">
    <h1>课程简介<button type="button" class="btn btn-primary btn-sm" @click="back()">返回</button></h1>
    <table border="1">
      <th>Course Title</th>
      <th>Teacher</th>
      <th>Class Room</th>
      <tr>
        <td>{{course.title}}</td>
        <td>{{course.teacher}}</td>
        <td>{{course.classroom}}</td>
      </tr>
    </table>
    <div id="courseInfo">
      <span v-html="message"></span>
    </div>
    <br />
    <button type="button" class="btn btn-primary btn-sm" @click="back()">返回</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Secure",
  data() {
    return {
      course: {},
      link: "",
      message: "课程介绍尽快出炉。敬请期待。谢谢🙏",
    };
  },
  methods: {
    back() {
      this.$router.replace({ name: "courses" });
    },
    load(filename) {
      const path = `http://localhost:5000/files/${filename}`;
      axios.get(path)
        .then((res) => {
          this.message = res.data.html;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  mounted() {
    this.course = this.$store.getters.COURSE;
    this.link = this.course["infolink"];
    this.load(this.link);
  }
};
</script>

<style scoped>
#secure {
  background-color: #ffffff;
  border: 1px solid #cccccc;
  padding: 20px;
  margin-top: 10px;
}
</style>