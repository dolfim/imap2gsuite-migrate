<template>
  <div class="main">

    <section class="section">
      <div class="container">
        <div class="content">
          <p class="content">
            <span class="is-3">Welcome <strong>{{ user.firstName }}</strong>,</span><br />
            Here you have the possibility to migrate all your emails and
            folders from the previous account to the new GSuite account.
          </p>
          <p>
            next item
          </p>
        </div>

        <div class="columns">
          <div class="column is-5 is-offset-1">
            <div class="card">
              <header class="card-header">
                <h3 class="card-header-title is-centered is-size-4">
                  Start new migration
                </h3>
              </header>
              <div class="card-content">
                <form @submit.prevent="launchMigrate">
                  <div class="content">
                    <p class="subtitle">
                      Migrate your emails to the new system.
                    </p>
                      <b-field label="Previous email">
                          <b-input
                            placeholder="Email"
                            v-model="migrateSettings.sourceEmail"
                          ></b-input>
                      </b-field>
                      <b-field label="Previous password">
                          <b-input
                            placeholder="Password"
                            type="password" password-reveal
                            v-model="migrateSettings.sourcePassword"
                          ></b-input>
                      </b-field>
                      <b-field label="Target GSuite email">
                          <b-input disabled
                            v-model="migrateSettings.targetEmail"
                          ></b-input>
                      </b-field>
                      <b-button
                        native-type="submit"
                        class="is-fullwidth is-primary"
                      >
                        Migrate
                      </b-button>
                  </div>
                </form>
              </div>
            </div>
          </div>

          <div class="column is-5">
            <div class="card">
              <header class="card-header">
                <h3 class="card-header-title is-centered is-size-4">
                  Inspect previous migration
                </h3>
              </header>
              <div class="card-content">
                <form @submit.prevent="viewTask">
                  <div class="content">
                    <p class="subtitle">
                      Inspect the status of a previous migration.
                      <!-- Please provide the task-id of your migration. -->
                    </p>
                    <b-field label="Migration task">
                        <b-input placeholder="Task ID" v-model="taskIdInput">
                        </b-input>
                    </b-field>
                    <b-button
                      native-type="submit"
                      class="is-fullwidth is-info"
                    >
                      View
                    </b-button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { getModule } from 'vuex-module-decorators';
import Auth from '@/store/modules/auth';
import { GApiData } from 'vue-gapi';
import { postMailMigrationTask } from '@/api';
import { MigrationTask } from '@/store/models.d';

@Component
export default class Main extends Vue {
  private auth = getModule(Auth, this.$store)

  public migrateSettings: MigrationTask = {
    sourceEmail: '',
    sourcePassword: '',
    targetEmail: this.user.email,
  };

  public taskIdInput = '';

  get user() {
    return this.auth.user as GApiData;
  }

  public async launchMigrate() {
    console.log(this.migrateSettings);
    const task = await postMailMigrationTask(this.migrateSettings);
    // TODO: show message that task was posted!
    console.log(task);
    this.$router.push({
      name: 'Task',
      params: { taskId: task.id },
    });
  }

  public viewTask(): void {
    this.$router.push({
      name: 'Task',
      params: { taskId: this.taskIdInput },
    });
  }
}
</script>
