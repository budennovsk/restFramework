
import { createStore } from 'vuex'
import axios from 'axios'

const store = new createStore({
    state: {
        products: []
    },
    mutations: {
        SET_PRODUCTS: (state, products) => { state.products = products }
    },
    actions: {
        GET_PRODUCTS_API({commit}) {
            return axios('http://127.0.0.1:8000/', {
                method: "GET"
            }).then((products) =>{
                commit('SET_PRODUCTS', products.data);
            return products;
        })
    } 
    },
getters: {
    PRODUCTS(state){
        return state.products;
    }
},

});
export default store;