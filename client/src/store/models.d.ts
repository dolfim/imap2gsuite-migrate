
interface GsuiteUserName {
  fullName?: string;
  givenName: string;
  familyName: string;
}
export interface GsuiteUser {
  name: GsuiteUserName;
  primaryEmail: string;
  recoveryEmail?: string;
  password?: string;
  changePasswordAtNextLogin?: boolean;
}

export interface MigrationTask {
  sourceEmail: string;
  sourcePassword: string;
  targetEmail: string;
}

export interface TaskDetails {
  id: string;
  status: string;
  result: string | null;
  enqueuedAt?: string;
  startedAt?: string;
  endedAt?: string;
}

export interface ServerError {
  code: number;
  message: string;
}
