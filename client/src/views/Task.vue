<template>
  <div class="task-view">

    <section class="section">
      <div class="container">
        <h2 class="title">Migration task</h2>
        <p class="subtitle">
          Task ID <code>{{ taskId }}</code>
        </p>
        <div class="message is-info">
          <div class="message-body">
            <strong>Hint</strong> Copy the task ID to come back to this page.
          </div>
        </div>

        <b-field grouped>
            <div class="control">
              <b-taglist attached>
                  <b-tag type="is-dark">task ID</b-tag>
                  <b-tag type="is-primary">{{ taskId }}</b-tag>
              </b-taglist>
            </div>

            <div class="control">
              <b-taglist attached>
                  <b-tag type="is-dark">status</b-tag>
                  <b-tag :type="taskStatusTag">{{ task.status }}</b-tag>
              </b-taglist>
            </div>

            <div class="control" v-if="lastFetched && !taskTerminated">
              <b-taglist attached>
                  <b-tag type="is-dark">Last check</b-tag>
                  <b-tag type="is-light">{{ lastFetched }}</b-tag>
              </b-taglist>
            </div>
        </b-field>

        <b-field grouped>
            <div class="control">
              <b-taglist attached>
                  <b-tag type="is-dark">Submitted at</b-tag>
                  <b-tag type="is-light">{{ task.enqueuedAt }}</b-tag>
              </b-taglist>
            </div>

            <div class="control" v-if="task.startedAt">
              <b-taglist attached>
                  <b-tag type="is-dark">Started at</b-tag>
                  <b-tag type="is-light">{{ task.startedAt }}</b-tag>
              </b-taglist>
            </div>

            <div class="control" v-if="task.endedAt">
              <b-taglist attached>
                  <b-tag type="is-dark">Finished at</b-tag>
                  <b-tag type="is-light">{{ task.endedAt }}</b-tag>
              </b-taglist>
            </div>
        </b-field>

        <div style="position: relative; min-height:4em;">
          <h4 class="is-size-4">Full output of the migration</h4>
          <pre
            v-if="task.result"
            v-bind:class="{ 'failed-log': task.status == 'failed' }"
          >
{{ task.result }}
          </pre>
          <b-loading
            :is-full-page="false"
            :active="!taskTerminated"
            :can-cancel="false"
          ></b-loading>
        </div>

      </div>
    </section>

  </div>
</template>

<script lang="ts">
import { Component, Watch, Vue } from 'vue-property-decorator';
import { getModule } from 'vuex-module-decorators';
import Auth from '@/store/modules/auth';
import { getTaskStatus } from '@/api';
import { TaskDetails, ServerError } from '@/store/models.d';

// Possible values are queued, started, deferred, finished, and failed

@Component
export default class Task extends Vue {
  private auth = getModule(Auth, this.$store)

  public task: TaskDetails = {
    id: 'new',
    result: null,
    status: 'unknown',
  };

  public lastFetched = '';

  get taskId() {
    return this.$route.params.taskId;
  }

  get taskStatusTag(): string {
    if (this.task.status === 'queued') {
      return 'is-info';
    }
    if (this.task.status === 'started') {
      return 'is-info';
    }
    if (this.task.status === 'finished') {
      return 'is-success';
    }
    if (this.task.status === 'failed') {
      return 'is-danger';
    }
    return 'is-light';
  }

  get taskTerminated(): boolean {
    if (this.task.status === 'finished') {
      return true;
    }
    if (this.task.status === 'failed') {
      return true;
    }
    return false;
  }

  mounted() {
    this.fetchTask();
  }

  @Watch('taskId')
  taskIdChanged(newTaskId: string) {
    if (newTaskId) {
      console.log('Value of taskId changed');
      this.fetchTask();
    }
  }

  public async fetchTask(): Promise<void> {
    try {
      this.task = await getTaskStatus(this.taskId);
      this.lastFetched = new Date().toUTCString();
      if (!this.taskTerminated) {
        setTimeout(() => this.fetchTask(), 4000);
      }
    } catch (err) {
      console.error(err);
      this.$buefy.snackbar.open({
        duration: 120000,
        message: `Error ${err.code}. ${err.message}`,
        type: 'is-danger',
        position: 'is-bottom-left',
      });
    }
  }
}
</script>

<style scoped>
.failed-log {
  background-color: hsl(348, 100%, 91%);
}
</style>
