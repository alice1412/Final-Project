import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import Register from '../views/Register.vue'
import Convert from '../views/Convert.vue'
import MindMap from '../views/MindMap.vue'
import MMEdit from '../views/MMEdit.vue'

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/convert',
        name: 'convert',
        component: Convert,
        meta: {
            requiresLogin: true
        }
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/logout',
        name: 'logout',
        component: Logout,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
    {
        path: "/mindmap",
        name: "MindMap",
        component: MindMap,
    },
    {
        path: "/mmedit/:index",
        name: "MMEdit",
        component: MMEdit,
    },
    {
        path: '*',
        redirect: "/"
    },
  ]
});

export default router