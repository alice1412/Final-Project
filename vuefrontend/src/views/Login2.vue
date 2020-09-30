<template>
  <div>
    <NavBar />
    <div class="login">
      <div class="box p-4">
        <h2>Login</h2>
        <p v-if="incorrectAuth">
          Incorrect username or password entered
          <br />
          Please try again
        </p>
        <form action @submit.prevent="SubmitHandler">
          <div class="form-group">
            <label for="username">Account :</label>
            <input
              type="text"
              name="username"
              id="user"
              class="form-control"
              v-model="username"
              placeholder="Username"
            />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input
              type="password"
              name="password"
              id="pass"
              class="form-control"
              v-model="password"
              placeholder="Password"
            />
          </div>
          <input type="submit" value="Submit" class="btn btn-dark" />
        </form>
        <p>
          No account yet?
          <router-link :to="{ name: 'register' }">Register Now!</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/Navbar-Top-After/index.vue";

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  components: {
    NavBar,
  },
  // 在生成頁面的時候透過此cookie判斷是否為登入狀態
  // username 為後端傳過來的資料
  // mounted() {
  //   let allCookies = document.cookie;
  //   if (allCookies.indexOf("username") !== -1) {
  //     this.$router.push("/convert");
  //   }
  // },
  methods: {
    SubmitHandler() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "posts" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>

<style scoped>
.login {
  width: 100%;
  height: 92vh;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 50%;
  height: 400px;
  position: relative;
  top: 100px;
}
.box .btn {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 15px;
  background: #fa5959;
  border: none;
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
@media screen and (max-width: 760px) {
  .login {
    height: 110vh;
  }
  .box {
    width: 70%;
    height: 70%;
    margin-bottom: 30px;
  }
}
@media screen and (max-height: 500px) {
  .login {
    height: 170vh;
  }
}
</style>