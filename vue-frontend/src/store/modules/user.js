import { getAPI } from '../../axios-api'

// state 的 APIData 為 Posts 裡面的資料
// APIData: '',
const state = {
    accessToken: null,
    refreshToken: null,
    APIFile:'',
    MindMap: null
}

const getters = {
    loggedIn(state) {
        return state.accessToken != null
    }
}

const mutations = {
    updateStorage(state, { access, refresh }) {
        state.accessToken = access
        state.refreshToken = refresh
    },
    destroyToken(state) {
        state.accessToken = null
        state.refreshToken = null
    }
}

const actions = {
    userLogout(context) {
        if (context.getters.loggedIn) {
            context.commit('destroyToken')
        }
    },
    userLogin(context, usercredentials) {
        return new Promise((resolve, reject) => {
            getAPI
                .post('/api-token/', {
                    username: usercredentials.username,
                    password: usercredentials.password
                })
                .then(response => {
                    context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
        })
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}