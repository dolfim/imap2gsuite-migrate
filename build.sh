#!/bin/bash

source .env
source config.env
if [ -f config.env.local ]; then
  source config.env.local
fi

echo "VUE_APP_OAUTH2_CLIENT_ID=${OAUTH2_CLIENT_ID}" > client/.env.production.local

docker build -t ${FRONTEND_IMAGE_NAME} -f Dockerfile-frontend .
docker build -t ${BACKEND_IMAGE_NAME} -f Dockerfile-backend .
