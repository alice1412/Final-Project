import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user' // 引入modules

Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        user
    }, // 放到這裡
})

export default store