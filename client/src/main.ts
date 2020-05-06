import Vue from 'vue';

import Buefy from 'buefy';
import VueGAPI from 'vue-gapi';
import 'buefy/dist/buefy.css';

import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.use(Buefy);

// import the plugin
const apiConfig = {
  // apiKey: '',
  clientId: process.env.VUE_APP_OAUTH2_CLIENT_ID,
  discoveryDocs: [],
  scope: 'email profile',
};

Vue.use(VueGAPI, apiConfig);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
