import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

background_task = Celery('conf')
background_task.config_from_object('django.conf:settings', namespace='CELERY')
background_task.autodiscover_tasks()

background_task.conf.beat_schedule = {
    'send-email-from-celery-beat': {
        'task': 'shop.tasks.send_spam_text'
    },
}

# Запуск рассылки спама по расписанию
background_task.conf.beat_schedule = {
    'send-email-from-celery-beat': {
        'task': 'shop.tasks.send_spam',
        'schedule': crontab(minute='*/2'),
    },
}