<template>
  <div id="app">
    <main>
      <!-- <b-navbar>
          <template slot="brand">
              <b-navbar-item tag="router-link" :to="{ path: '/' }">
                  <img
                      src="./assets/science-olympiad-logo.png"
                      alt="Email Migration"
                  >
              </b-navbar-item>
          </template>
      </b-navbar> -->
      <section class="hero is-light">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Science Olympiad Email Migration
            </h1>
            <h2 class="subtitle">
              Migrate your emails to the new GSuite infrastructure
            </h2>
          </div>
        </div>
      </section>

      <router-view />

      <footer class="footer">
        <div class="content has-text-centered">
          <p>
            <strong>Science.Olympiad Email Migration</strong>, a management tool
            for the Science Olympiad.
          </p>
        </div>
      </footer>
    </main>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { getModule } from 'vuex-module-decorators';
import Auth from '@/store/modules/auth';

@Component
export default class App extends Vue {
  private auth = getModule(Auth, this.$store)

  created() {
    this.auth.init();
  }
}
</script>
