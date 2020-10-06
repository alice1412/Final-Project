import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
// import store from './store'
import store from '../../vuefrontend/src/store/index'
import IdleVue from 'idle-vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

//ScrollTo
const VueScrollTo = require("vue-scrollto");
Vue.use(VueScrollTo);
Vue.config.productionTip = false;

// import 'jsmind'
import jm from '../dist/build'
Vue.use(jm)
// import jm from "vue-jsmind";
// Vue.use(jm);

const eventsHub = new Vue()

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 5000
})

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
