#!/usr/bin/env python

from celery import Celery

celery = Celery('mytask',
                broker='amqp://localhsot//'
                )
celery.conf.update(
    CELERY_RESULT_BACKEND="amqp://localhost//",
)


@celery.task
def add(x, y):
    return x + y
