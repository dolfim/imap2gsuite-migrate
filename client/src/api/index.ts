import axios, { AxiosError } from 'axios';
import { TaskDetails, ServerError, MigrationTask } from '@/store/models.d';

import { getModule } from 'vuex-module-decorators';
import store from '@/store';
import Auth from '@/store/modules/auth';

const auth = getModule(Auth, store);

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use((config) => {
  // eslint-disable-next-line no-param-reassign
  config.headers.Authorization = auth.token;
  return config;
});


export const getTaskStatus = async (taskId: string): Promise<TaskDetails> => {
  try {
    const response = await apiClient.get<TaskDetails>(`/task/${taskId}`);
    const task = response.data;
    console.log('task:', task);
    console.log('task.id:', task.id);
    console.log('task.status:', task.status);
    return task;
  } catch (err) {
    if (err && err.response) {
      const axiosError = err as AxiosError<ServerError>;
      if (axiosError.response) {
        throw axiosError.response.data;
      }
    }

    throw err;
  }
};

export const postMailMigrationTask = async (mig: MigrationTask): Promise<TaskDetails> => {
  try {
    const response = await apiClient.post<TaskDetails>('/task', mig);
    const task = response.data;
    return task;
  } catch (err) {
    if (err && err.response) {
      const axiosError = err as AxiosError<ServerError>;
      if (axiosError.response) {
        throw axiosError.response.data;
      }
    }

    throw err;
  }
};
