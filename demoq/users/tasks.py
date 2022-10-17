from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
import string
from django.utils.crypto import get_random_string
from celery import shared_task, current_task

User = get_user_model()


@shared_task
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()

@shared_task
def create_random_user_accounts(total_user):
    for i in range(total_user):
        username = 'user_%s' % get_random_string(20, string.ascii_letters)
        email = '%s@example.com' % username
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
        percent = int((float(i) / total_user) * 100)
        current_task.update_state(state='PROGRESS',
                                  meta={'current': i, 'total': total_user,
                                        'percent': percent})
        print({'current': i, 'total': total_user, 'percent': percent})
    return {'current': total_user, 'total': total_user, 'percent': 100}

