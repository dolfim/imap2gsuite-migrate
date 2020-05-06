#!/bin/bash
REDIS_URL=${REDIS_URL:-"redis://localhost:6379/"}
LOG_LEVEL=${LOG_LEVEL:-"INFO"}
exec rq worker --url="${REDIS_URL}" --disable-job-desc-logging --logging_level="${LOG_LEVEL}"
