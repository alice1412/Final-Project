import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Posts from './views/Posts'
import Login from './views/Login2'
import Logout from './views/Logout'
import Register from './views/RegisterV2'
import Convert from './views/Convert'
import Settings from './views/Settings'
import MindMap from './views/MindMap'
import MMEdit from './views/MMEdit'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
        },
        {
            path: '/posts',
            name: 'posts',
            component: Posts,
            meta: {
                requiresLogin: true
            }
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
            path: '/settings',
            name: 'settings',
            component: Settings,
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
})