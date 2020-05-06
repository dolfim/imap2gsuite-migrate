#!/bin/bash

export PORT=${PORT:-"5000"}

exec gunicorn -b 0.0.0.0:$PORT -k gevent server.app:app
