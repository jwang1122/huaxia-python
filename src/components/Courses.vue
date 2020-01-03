<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>华夏中文学校-糖城分校-中文课程        
          <button 
          type="button" 
          class="btn btn-success btn-sm" 
          v-if="user['rule']=='admin'"
          v-b-modal.class-modal>增加课程</button></h2>
        <alert :message=message v-if="showMessage"></alert>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">课程名称</th>
              <th scope="col">主讲教师</th>
              <th scope="col">教室编号</th>
              <th scope="col">学期学费</th>
              <th scope="col">课程链接</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(course, index) in courses" :key="index">
              <td>{{ course.title }}</td>
              <td>{{ course.teacher }}</td>
              <td>{{ course.classroom }}</td>
              <td>${{ course.price }}</td>
              <td>
                 <button 
                          type="button"
                          class="btn btn-primary btn-sm"
                          @click="getCourseInfo(course)">
                      简介
                  </button>

              </td>
              <td>
                <div class="btn-group" role="group">
                  <button 
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.class-update-modal
                          v-if="user['rule']=='admin'"
                          @click="editClass(course)">
                      修改
                  </button>
                  <button
                          type="button"
                          v-if="user['rule']=='admin'"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteClass(course)">
                      删除
                  </button>
                  <router-link :to="`/order/${course._id}`"
                              v-if="user['rule']!='admin'"
                              class="btn btn-primary btn-sm">
                      交纳学费
                  </router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addClassModal"
            id="class-modal"
            title="增加新课程"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="课程名称:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addClassForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-teacher-group"
                      label="主讲教师:"
                      label-for="form-teacher-input">
            <b-form-input id="form-teacher-input"
                          type="text"
                          v-model="addClassForm.teacher"
                          required
                          placeholder="输入教师姓名">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-classroom-group"
                      label="教室编号:"
                      label-for="form-classroom-input">
            <b-form-input id="form-classroom-input"
                          type="text"
                          v-model="addClassForm.classroom"
                          required
                          placeholder="输入教室编号">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-infolink-group"
                      label="课程简介:"
                      label-for="form-infolink-input">
            <b-form-input id="form-infolink-input"
                          type="text"
                          v-model="addClassForm.infolink"
                          required
                          placeholder="Enter infolink">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-price-group"
                        label="学费:"
                        label-for="form-price-input">
            <b-form-input id="form-price-input"
                          type="number"
                          step="0.01"
                          v-model="addClassForm.price"
                          required
                          placeholder="Enter price">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">确认增加</b-button>
          <b-button type="reset" variant="danger">重新输入</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editClassModal"
            id="class-update-modal"
            title="修改课程"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="课程名称:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-teacher-edit-group"
                      label="教师姓名:"
                      label-for="form-teacher-edit-input">
            <b-form-input id="form-teacher-edit-input"
                          type="text"
                          v-model="editForm.teacher"
                          required
                          placeholder="Enter teacher name">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-classroom-edit-group"
                      label="教室编号:"
                      label-for="form-classroom-edit-input">
            <b-form-input id="form-classroom-edit-input"
                          type="text"
                          v-model="editForm.classroom"
                          required
                          placeholder="Enter classroom">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-classroom-edit-group"
                      label="课程简介:"
                      label-for="form-classroom-edit-input">
            <b-form-input id="form-classroom-edit-input"
                          type="text"
                          v-model="editForm.infolink"
                          required
                          placeholder="Enter infolink">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-price-edit-group"
                        label="学期学费:"
                        label-for="form-price-edit-input">
            <b-form-input id="form-price-edit-input"
                          type="text"
                          v-model="editForm.price"
                          required
                          placeholder="输入学期学费">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">确认修改</b-button>
          <b-button type="reset" variant="danger">放弃修改</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      user:{},
      courses: [],
      addClassForm: {
        title: '',
        teacher: '',
        classroom: '',
        infolink:'',
        price: 0,
      },
      message: '',
      showMessage: false,
      editForm: {
        _id: '',
        title: '',
        teacher: '',
        classroom: '',
        infolink: '',
        price: 0,
      },
    };
  },
  components: {
    alert: Alert,
  },
  mounted() {
    this.user = this.$store.getters.USER;
//    alert("@JWANG: user rule: " + this.user['rule']);
  },
  methods: {
    getCourses() {
      const path = 'http://localhost:5000/courses';
      axios.get(path)
        .then((res) => {
          this.courses = res.data.courses;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addClass(payload) {
      const path = 'http://localhost:5000/courses';
      axios.post(path, payload)
        .then(() => {
          this.getCourses();
          this.message = '新课程成功加入!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCourses();
        });
    },
    initForm() {
      this.addClassForm.title = '';
      this.addClassForm.teacher = '';
      this.addClassForm.classroom = '';
      this.editForm._id = '';
      this.editForm.title = '';
      this.editForm.teacher = '';
      this.editForm.classroom = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addClassModal.hide();
      const payload = {
        title: this.addClassForm.title,
        teacher: this.addClassForm.teacher,
        price: this.addClassForm.price,
        classroom: this.addClassForm.classroom, // property shorthand
        infolink: this.addClassForm.infolink,
      };
      this.addClass(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addClassModal.hide();
      this.initForm();
    },
    editClass(course) {
      this.editForm = course;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editClassModal.hide();
      const payload = {
        title: this.editForm.title,
        teacher: this.editForm.teacher,
        price: this.editForm.price,
        classroom: this.editForm.classroom,
        infolink: this.addClassForm.infolink,
      };
      this.updateClass(payload, this.editForm._id);
    },
    updateClass(payload, classID) {
      const path = `http://localhost:5000/courses/${classID}`;
      axios.put(path, payload)
        .then(() => {
          this.getCourses();
          this.message = '课程完成修正!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getCourses();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editClassModal.hide();
      this.initForm();
      this.getCourses(); // why?
    },
    removeClass(classID) {
      const path = `http://localhost:5000/courses/${classID}`;
      axios.delete(path)
        .then(() => {
          this.getCourses();
          this.message = '课程成功被删除!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getCourses();
        });
    },
    onDeleteClass(course) {
      this.removeClass(course._id);
    },
    getCourseInfo(course){
       this.$store.commit("SET_COURSE", course);
      this.$router.replace({ name: "secure" });
    },
  },
  created() {
    this.getCourses();
  },
};
</script>
