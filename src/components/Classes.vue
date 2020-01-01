<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>中文课程</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.class-modal>增加课程</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">课程名称</th>
              <th scope="col">主讲教师</th>
              <th scope="col">教室</th>
              <th scope="col">学费</th>
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
                  <router-link :to="`/order/${class0.id}`"
                              class="btn btn-primary btn-sm">
                      加纳学费
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
            title="Add a new class"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addClassForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addClassForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-price-group"
                        label="Purchase price:"
                        label-for="form-price-input">
            <b-form-input id="form-price-input"
                          type="number"
                          step="0.01"
                          v-model="addClassForm.price"
                          required
                          placeholder="Enter price">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addClassForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editClassModal"
            id="class-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-price-edit-group"
                        label="Purchase price:"
                        label-for="form-price-edit-input">
            <b-form-input id="form-price-edit-input"
                          type="text"
                          v-model="editForm.price"
                          required
                          placeholder="Enter price">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
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
        id: '',
        title: '',
        author: '',
        read: [],
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
          this.message = 'Class added!';
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
      this.addClassForm.author = '';
      this.addClassForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addClassModal.hide();
      let read = false;
      if (this.addClassForm.read[0]) read = true;
      const payload = {
        title: this.addClassForm.title,
        author: this.addClassForm.author,
        price: this.addClassForm.price,
        read, // property shorthand
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
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        price: this.editForm.price,
        read,
      };
      this.updateClass(payload, this.editForm.id);
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
      this.removeClass(class0.id);
    },
  },
  created() {
    this.getClasses();
  },
};
</script>
