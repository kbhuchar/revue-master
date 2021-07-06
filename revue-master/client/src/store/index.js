import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import UsersService from '@/services/UsersService'

// GUIDE: The store contains data that will be available across the app
// Values are reactive, so if a component reads a value which later changes,
// the component will automatically receive the new value   
// You cannot directly change the state of the store. instead you have to use a
// commit function to do so.
export default Vuex.createStore({
    plugins: [createPersistedState()],

    state: {
        token: null,
        user: null,
        isUserLoggedIn: false,
        subscribedSubvues: [],
        selectedService: []
    },

    mutations: {
        setToken(state, token) {
            state.token = token
            if (token) {
                state.isUserLoggedIn = true
            } else {
                state.isUserLoggedIn = false
            }
        },
        setUser(state, user) {
            state.user = user
        },
        setSubscribedSubvues(state, subvues) {
            state.subscribedSubvues = subvues
        },
        setServiceState(state, newS) {
            state.selectedService = newS
        },
    },

    actions: {
        setServiceState({ commit }, state) {
            commit('setServiceState', state)
        },
        setToken({ commit }, token) {
            commit('setToken', token)
        },
        setUser({ commit }, user) {
            commit('setUser', user)
        },
        updateSubscribedSubvues({ commit, state }, subscribedOptional) {
            if (state.isUserLoggedIn) {
                if (subscribedOptional) {
                    // If data was provided
                    commit('setSubscribedSubvues', subscribedOptional)
                } else {
                    UsersService.username(state.user.username)
                        .then(response => {
                            commit('setSubscribedSubvues', response.data.subscribed)
                        })
                        .catch(() => {
                            // console.error(e)
                        })
                }
            }
        }
    },

    modules: {
    }
});
