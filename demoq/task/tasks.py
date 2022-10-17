from __future__ import absolute_import, unicode_literals
from celery import Celery, app, shared_task

from kombu import Exchange, Queue
from celery.exceptions import Reject


# @task(name="ADD")
@shared_task
def add(x,y):
    return x + y


# @task(name="MUL")
@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

