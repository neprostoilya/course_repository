from django.core.mail import send_mail
from conf import settings

def send(email):
    """Отправка спама на почту"""
    send_mail(
        subject='shop.spam.uz',
        message="Вы подписались на спам рассылку и мы будем вам спамить😈",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )



