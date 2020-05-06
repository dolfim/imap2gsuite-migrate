import Vue from 'vue';
import {
  VuexModule, Module, Mutation, Action,
} from 'vuex-module-decorators';
import { GApiData } from 'vue-gapi';

@Module({ namespaced: true, name: 'auth' })
class Auth extends VuexModule {
  public initialized = false;

  public authenticated = false;

  public user: GApiData | null = null;

  public token = '';

  @Mutation
  public setInitialized(newValue: boolean): void {
    this.initialized = newValue;
  }

  @Mutation
  public setUser(newValue: GApiData): void {
    this.user = newValue;
    if (this.user != null) {
      this.token = this.user.idToken;
    } else {
      this.token = '';
    }
  }

  @Mutation
  public setAuthenticated(newValue: boolean): void {
    this.authenticated = newValue;
  }

  @Action({ rawError: true })
  public async init(): Promise<any> {
    const gapi = await Vue.prototype.$gapi.getGapiClient();
    if (Vue.prototype.$gapi.isAuthenticated()) {
      this.context.commit('setUser', Vue.prototype.$gapi.getUserData());
      this.context.commit('setAuthenticated', true);
    } else {
      this.context.commit('setUser', null);
      this.context.commit('setAuthenticated', false);
    }
    this.context.commit('setInitialized', true);
  }

  @Action({ rawError: true })
  public async login(res: Function): Promise<any> {
    if (!this.authenticated) {
      return Vue.prototype.$gapi
        .login(() => {
          // eslint-disable-next-line no-console
          console.log('Successfully authenticated');
          this.context.commit('setUser', Vue.prototype.$gapi.getUserData());
          this.context.commit('setAuthenticated', true);
          // this.userData = this.$gapi.getUserData();
          res();
        })
        .catch((err: any) => {
          this.context.commit('setUser', null);
          this.context.commit('setAuthenticated', false);
          // eslint-disable-next-line no-console
          console.error('Login call failed: %s', err.message);
        });
    }
    console.log('Authenticated is true!');
    return null;
    // return new Promise((resolve, _reject) => resolve());
  }
}

export default Auth;
