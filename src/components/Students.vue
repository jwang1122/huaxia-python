<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h2>华夏中文学校-糖城分校-学生登记表       
          <button 
          type="button" 
          class="btn btn-success btn-sm" 
          v-if="user['rule']=='admin'"
          v-b-modal.student-modal>增加新学生</button></h2>
        <alert :message=message v-if="showMessage"></alert>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">学生姓名</th>
              <th scope="col">年龄</th>
              <th scope="col">性别</th>
              <th scope="col">家长姓名</th>
              <th scope="col">联系电话</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(student, index) in students" :key="index">
              <td>{{ student.fullname }}</td>
              <td>{{ student.age }}</td>
              <td>{{ student.gender }}</td>
              <td>{{ student.parentname }}</td>
               <td>{{ student.phone }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button 
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.class-update-modal
                          v-if="user['rule']=='admin'"
                          @click="editStudent(student)">
                      修改
                  </button>
                  <button
                          type="button"
                          v-if="user['rule']=='admin'"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteStudent(student)">
                      删除
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addStudentModal"
            id="student-modal"
            title="增加新学生"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-fullname-group"
                    label="学生姓名:"
                    label-for="form-fullname-input">
          <b-form-input id="form-fullname-input"
                        type="text"
                        v-model="addStudentForm.fullname"
                        required
                        placeholder="Enter fullname">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-age-group"
                      label="年龄:"
                      label-for="form-age-input">
            <b-form-input id="form-age-input"
                          type="text"
                          v-model="addStudentForm.age"
                          required
                          placeholder="Enter age">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-gender-group"
                      label="性别:"
                      label-for="form-gender-input">
            <b-form-input id="form-gender-input"
                          type="text"
                          v-model="addStudentForm.gender"
                          required
                          placeholder="Enter gender">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-parentname-group"
                      label="家长姓名:"
                      label-for="form-parentname-input">
            <b-form-input id="form-parentname-input"
                          type="text"
                          v-model="addStudentForm.parentname"
                          required
                          placeholder="Enter parent name.">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-phone-group"
                        label="联系电话:"
                        label-for="form-phone-input">
            <b-form-input id="form-phone-input"
                          type="text"
                           v-model="addStudentForm.phone"
                          required
                          placeholder="Enter phone">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">确认增加</b-button>
          <b-button type="reset" variant="danger">重新输入</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editStudentModal"
            id="class-update-modal"
            title="修改学生记录"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-fullname-edit-group"
                    label="学生姓名:"
                    label-for="form-fullname-edit-input">
          <b-form-input id="form-fullname-edit-input"
                        type="text"
                        v-model="editForm.fullname"
                        required
                        placeholder="Enter fullname">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-age-edit-group"
                      label="年龄:"
                      label-for="form-age-edit-input">
            <b-form-input id="form-age-edit-input"
                          type="text"
                          v-model="editForm.age"
                          required
                          placeholder="Enter age name">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-gender-edit-group"
                      label="性别:"
                      label-for="form-gender-edit-input">
            <b-form-input id="form-gender-edit-input"
                          type="text"
                          v-model="editForm.gender"
                          required
                          placeholder="Enter gender">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-parentname-edit-group"
                      label="家长姓名:"
                      label-for="form-parentname-edit-input">
            <b-form-input id="form-parentname-edit-input"
                          type="text"
                          v-model="editForm.parentname"
                          required
                          placeholder="Enter parent name">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-phone-edit-group"
                        label="联系电话:"
                        label-for="form-phone-edit-input">
            <b-form-input id="form-price-phone-input"
                          type="text"
                          v-model="editForm.phone"
                          required
                          placeholder="phone">
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
      students: [],
      addStudentForm: {
        fullname: '',
        age: '',
        gender: '',
        parentname:'',
        phone: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        _id: '',
        fullname: '',
        age: '',
        gender: '',
        parentname: '',
        phone: '',
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
    getStudents() {
      const path = 'http://localhost:5000/students';
      axios.get(path)
        .then((res) => {
          this.students = res.data.students;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addStudent(payload) {
      const path = 'http://localhost:5000/students';
      axios.post(path, payload)
        .then(() => {
          this.getStudents();
          this.message = '新课程成功加入!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getStudents();
        });
    },
    initForm() {
      this.addStudentForm.fullname = '';
      this.addStudentForm.age = '';
      this.addStudentForm.gender = '';
      this.editForm._id = '';
      this.editForm.fullname = '';
      this.editForm.age = '';
      this.editForm.gender = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addStudentModal.hide();
      const payload = {
        fullname: this.addStudentForm.fullname,
        age: this.addStudentForm.age,
        phone: this.addStudentForm.phone,
        gender: this.addStudentForm.gender, // property shorthand
        parentname: this.addStudentForm.parentname,
      };
      this.addStudent(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addStudentModal.hide();
      this.initForm();
    },
    editStudent(student) {
      this.editForm = student;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editStudentModal.hide();
      const payload = {
        fullname: this.editForm.fullname,
        age: this.editForm.age,
        phone: this.editForm.phone,
        gender: this.editForm.gender,
        parentname: this.addStudentForm.parentname,
      };
      this.updateStudent(payload, this.editForm._id);
    },
    updateStudent(payload, studentID) {
      const path = `http://localhost:5000/students/${studentID}`;
      axios.put(path, payload)
        .then(() => {
          this.getStudents();
          this.message = '完成修正!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getStudents();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editStudentModal.hide();
      this.initForm();
      this.getStudents(); // why?
    },
    remove(studentID) {
      const path = `http://localhost:5000/students/${studentID}`;
      axios.delete(path)
        .then(() => {
          this.getStudents();
          this.message = '学生成功被删除!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getStudents();
        });
    },
    onDeleteStudent(student) {
      this.removeStudent(student._id);
    },
    getStudentInfo(student){
       this.$store.commit("SET_student", student);
      this.$router.replace({ name: "secure" });
    },
  },
  created() {
    this.getStudents();
  },
};
</script>
