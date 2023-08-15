from conf.celery import background_task as task
from django.core.mail import send_mail

from .models import Mail
from .service import send
from conf import settings

@task.task
def send_message(email):
    """Запуск в фоновом режиме"""
    send(email)
    
@task.task
def send_spam_text(text):
    """Запуск рассылки спама """
    users = Mail.objects.all()
    for user in users:
        send_mail(
            subject='shop.spam.uz',
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=False
        )

@task.task
def send_spam():
    """Запуск рассылки спама по расписанию"""
    users = Mail.objects.all()
    for user in users:
        send_mail(
            subject='Спам',
            message='Переодический Спам',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=False
        )

