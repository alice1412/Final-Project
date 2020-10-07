<template>
  <div>
    <NavBar />
    <div class="login">
      <div class="box p-4">
        <h2>Register</h2>
        <form action @submit="SubmitHandler" @reset="ResetHandler">
          <div class="form-group">
            <label for="username">Account :</label>
            <input
              type="text"
              name="username"
              id="username"
              class="form-control"
              v-model="username"
              required
            />
          </div>
          <div class="form-group">
            <label for="email">E-mail :</label>
            <input
              type="email"
              name="email"
              id="email"
              class="form-control"
              v-model="email"
              required
            />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input
              type="password"
              name="password"
              id="password"
              class="form-control"
              v-model="password"
              required
            />
          </div>
          <div class="form-group">
            <label for="pwd-confirm">Confirm Password :</label>
            <input
              type="password"
              id="pwd-confirm"
              class="form-control"
              v-model="confirm"
              required
            />
          </div>
          <div class="btn-group d-flex">
            <input type="reset" value="Reset" class="btn btn-dark" />
            <input type="submit" value="Submit" class="btn btn-dark" />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/Navbar-Top-After/index.vue";
import { getAPI } from "../axios-api";
// import Cookies from "js-cookie";

export default {
  name: "Register",
  components: {
    NavBar,
  },
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirm: "",
    };
  },
  methods: {
    ResetHandler(evt) {
      evt.preventDefault();
      (this.username = ""),
        (this.email = ""),
        (this.password = ""),
        (this.confirm = "");
    },
    SubmitHandler(evt) {
      evt.preventDefault();
      //   -----封裝將傳出的資料-----
      // let csrftoken = Cookies.get("csrftoken");
      // let axiosConfig = {
      //   headers: {
      //     // "X-CSRFToken": csrftoken,
      //     "content-type": "application/json",
      //   },
      // };
      // "content-type": "application/x-www-form-urlencoded",
      // Authorization: localStorage.getItem("jwtToken"),
      let postData = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      const myFormData = new FormData();
      myFormData.append("postData", JSON.stringify(postData));

      //-----判斷並傳送資料-----
      if (this.password != this.confirm) {
        alert("Please check your password before you submit");
      } else {
        alert("Successfully registered!");
        getAPI
          .post("/api/users/", postData)
          // .post("/api/users/", myFormData)
          .then((res) => {
            console.log(res);
            (this.username = ""),
              (this.email = ""),
              (this.password = ""),
              (this.confirm = "");
            this.$router.push("/login");
            console.log(res);
          })
          .catch((error) => {
            console.log(error);
            // console.log(error.response.request._response);
          });
      }
    },
  },
};
</script>

<style scoped>
.login {
  width: 100%;
  height: 140vh;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 50%;
  height: 600px;
  position: relative;
  top: 100px;
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
h2 {
  text-align: left;
}
.form-group {
  margin-top: 30px;
  margin-bottom: 30px;
  text-align: left;
}
@media screen and (max-height: 540px) {
  .login {
    height: 230vh;
  }
}
@media screen and (max-height: 360px) {
  .login {
    height: 260vh;
  }
}
@media screen and (max-height: 280px) {
  .login {
    height: 300vh;
  }
}
</style>
