#! /usr/bin/env bash

set -e

DEPLOY_MODE = "production"


if [ ${DEPLOY_MODE} = "production" ]; then
    rm /etc/nginx/conf.d/default.conf
    cp ./nginx.conf_production /etc/nginx/conf.d/nginx.conf
    gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 4 app.main:app
else

    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi
