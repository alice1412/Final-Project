<template>
  <div class="settings">
    <NavBar />
    <div class="row box p-4">
      <div class="col-12">
        <h2>User Settings</h2>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="mt-4">
          <b-form-group id="input-group-1" label="Name:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.name"
              required
              placeholder="Enter name"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Email:" label-for="input-2">
            <b-form-input
              id="input-2"
              type="email"
              v-model="form.email"
              placeholder="Enter email"
              required
            ></b-form-input>
          </b-form-group>
          <b-row class="mt-3 p-3">
            <b-button type="submit" class="btn btn-dark w-50">Save</b-button>
            <b-button type="reset" class="btn btn-dark w-50">Cancel</b-button>
          </b-row>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/Navbar-Top-New/index.vue";
import { getAPI } from "../axios-api";
// import { mapState } from "vuex";

export default {
  name: "Settings",
  components: {
    NavBar,
  },
  computed: {},
  // created() {
  //   getAPI
  //     .get("/posts/", {
  //       headers: {
  //         // Authorization: `Bearer ${this.$store.state.user.accessToken}`,
  //       },
  //     })
  //     .then((response) => {
  //       // response user 的 username 和 email
  //       // this.$store.state.模組.狀態 = response.data
  //       // EX : this.$store.state.user.APIData = response.data;
  //       this.$store.state.user.APIData = response.data;
  //       console.log(response.data);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // },
  data() {
    return {
      form: {
        name: "",
        email: "",
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
      getAPI
        .post("/posts/", {
          name: this.form.name,
          email: this.form.email,
        })
        .then((response) => {
          this.form.name = null;
          this.form.email = null;
          // this.form.push("response.data");
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
      // 舊版寫法
      // this.$axios
      //   .post("http://localhost:3000/user-info", {
      //     name: this.form.name,
      //     email: this.form.email,
      //   })
      //   .then((res) => {
      //     (this.form.name = ""),
      //       (this.form.email = ""),
      //       // this.form.push("res.data");
      //       console.log(res);
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //   });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.email = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>

<style scoped>
.settings {
  width: 90vw;
  height: 90vh;
  margin: auto;
  align-items: center;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 80%;
  height: 90%;
  position: relative;
  margin-top: 100px;
  text-align: left;
}
.box .btn {
  margin-top: 10px;
  margin-bottom: 15px;
  background: #fa5959;
  border: 2px solid #ffffff;
  transition: 0.2s;
}
.box .btn:hover {
  background: #d01414;
}
.box p {
  text-align: center;
}
</style>