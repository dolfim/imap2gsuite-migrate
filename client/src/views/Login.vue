<template>
  <section class="section">
    <div class="container">
      <div class="columns is-mobile">
        <div class="column is-half is-offset-one-quarter">
          <div class="card">
            <header class="card-header">
              <h2 class="card-header-title is-centered title">
                Sign in
              </h2>
            </header>
            <div class="card-content">
              <div class="content">
                <p class="is-size-4">
                  You are currently logged out. Click on the button below to start
                  the sign.
                </p>
                <p class="has-text-centered">
                  <b-button
                    class="is-primary is-medium is-middle"
                    :loading="!authReady"
                    :disabled="authenticated"
                    @click="login"
                  >Login with GSuite</b-button>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { Component, Watch, Vue } from 'vue-property-decorator';
import { getModule } from 'vuex-module-decorators';
import Auth from '@/store/modules/auth';

@Component
export default class Login extends Vue {
  private auth = getModule(Auth, this.$store)

  get authReady() {
    return this.auth.initialized;
  }

  get authenticated() {
    return this.auth.authenticated;
  }

  @Watch('authReady')
  readyChanged(newReadyVal: boolean) {
    if (newReadyVal && this.authenticated) {
      console.log('Already authenticated');
      if (this.$route.params.nextUrl != null) {
        this.$router.push(this.$route.params.nextUrl);
      } else {
        this.$router.push({ name: 'Main' });
      }
    }
  }

  public login(): void {
    this.auth.login(() => {
      console.log('Success in login view!');
      if (this.$route.params.nextUrl != null) {
        this.$router.push(this.$route.params.nextUrl);
      } else {
        this.$router.push({ name: 'Main' });
      }
    })
      .catch((err: any) => {
        console.error('Error in login view.');
        console.error(err);
      });
  }
}
</script>
