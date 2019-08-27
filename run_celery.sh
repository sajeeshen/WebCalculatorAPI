#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd app
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
su  user -c "celery worker -A app.celeryconf -Q default -n default@%h"


docker-compose run app sh -c "celery worker -A app.celeryconf -Q default -n default@%h"
