declare module 'vue-gapi' {
    import { PluginFunction } from 'vue';

    // The `install` method is called inside Vue.use() function. It's required.
    export const install: PluginFunction<{}>;

    export interface GApiData {
      firstName: string;
      lastName: string;
      fullName: string;
      email: string;
      imageUrl: string;
      accessToken: string;
      idToken: string;
    }

    export interface GApi {
      logout: any;
      login: any;
      isAuthenticated: () => boolean;
      refreshToken: () => string;
      getGapiClient: () => Promise<GApi>;
      getUserData: () => GApiData;
      client: any;
    }

    // Add global object to Vue instance, so you can use `this.@login` etc.
    module 'vue/types/vue' {
        interface Vue {
            $gapi: GApi;
            // $logout: any,
            // $login: any,
            $getGapiClient: () => Promise<GApi>;
            // $isAuthenticated: any
        }
    }
}
