<template>
  <div>
    <div id="activities">
      <span v-html="message"></span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "activities",
  data() {
    return {
      message: "课程介绍尽快出炉。敬请期待。谢谢🙏"
    };
  },
  methods: {
    load() {
      const path = `http://localhost:5000/files/activities`;
      axios
        .get(path)
        .then(res => {
          this.message = res.data.html;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  mounted() {
    this.load();
  }
};
</script>
