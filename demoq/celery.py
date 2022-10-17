from __future__ import absolute_import
import os

from celery import Celery
from director import task
from kombu import Exchange, Queue
from celery.exceptions import Reject
# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("demoq")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.

default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'

sunshine_queue_name = 'sunshine'
sunshine_routing_key = 'sunshine'

moon_queue_name = 'moon'
moon_routing_key = 'moon'

# app = Celery(
#     broker='pyamqp://guest@localhost:5672//',)
#     # backend='redis://localhost:6379/0')

default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key)

sunshine_queue = Queue(
    sunshine_queue_name,
    default_exchange,
    routing_key=sunshine_routing_key)

moon_queue = Queue(
    moon_queue_name,
    default_exchange,
    routing_key=moon_queue_name)

app.conf.task_queues = (default_queue, sunshine_queue, moon_queue)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key


app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
