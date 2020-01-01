<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>华夏中文学校-糖城分校-中文课程</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.class-modal>增加课程</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">课程名称</th>
              <th scope="col">主讲教师</th>
              <th scope="col">教室编号</th>
              <th scope="col">学期学费</th>
              <th scope="col">课程简介</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(class0, index) in classes" :key="index">
              <td>{{ class0.title }}</td>
              <td>{{ class0.teacher }}</td>
              <td>{{ class0.classroom }}</td>
              <td>${{ class0.price }}</td>
              <td>{{ class0.description }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.class-update-modal
                          @click="editClass(class0)">
                      修改课程
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteClass(class0)">
                      删除课程
                  </button>
                  <router-link :to="`/order/${class0._id}`"
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
      classes: [],
      addClassForm: {
        title: '',
        teacher: '',
        classroom: '',
        price: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        _id: '',
        title: '',
        teacher: '',
        classroom: '',
        price: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getClasses() {
      const path = 'http://localhost:5000/classes';
      axios.get(path)
        .then((res) => {
          this.classes = res.data.classes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addClass(payload) {
      const path = 'http://localhost:5000/classes';
      axios.post(path, payload)
        .then(() => {
          this.getClasses();
          this.message = '新课程成功加入!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getClasses();
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
      };
      this.addClass(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addClassModal.hide();
      this.initForm();
    },
    editClass(class0) {
      this.editForm = class0;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editClassModal.hide();
      const payload = {
        title: this.editForm.title,
        teacher: this.editForm.teacher,
        price: this.editForm.price,
        classroom: this.editForm.classroom,
      };
      this.updateClass(payload, this.editForm._id);
    },
    updateClass(payload, classID) {
      const path = `http://localhost:5000/classes/${classID}`;
      axios.put(path, payload)
        .then(() => {
          this.getClasses();
          this.message = 'Class updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getClasses();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editClassModal.hide();
      this.initForm();
      this.getClasses(); // why?
    },
    removeClass(classID) {
      const path = `http://localhost:5000/classes/${classID}`;
      axios.delete(path)
        .then(() => {
          this.getClasses();
          this.message = 'Class removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getClasses();
        });
    },
    onDeleteClass(class0) {
      this.removeClass(class0._id);
    },
  },
  created() {
    this.getClasses();
  },
};
</script>
