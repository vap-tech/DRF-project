import os
from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail

from lms.models import Course
from users.models import User


@shared_task
def send_info(course: 'Course'):
    """Рассылка уведомлений об изменении курса"""
    subscriptions = course.subscription_set.all()
    for subscription in subscriptions:

        send_mail(
            'Курс обновлён!',
            'Привет, был обновлён, не забудь посмотреть что изменилось!',
            os.getenv('EMAIL_HOST_USER'),
            [subscription.user.email],
            fail_silently=True,
        )


def block_inactive_users():
    """Блокировка пользователей, неактивных более 3 месяцев"""
    for user in User.objects.all():
        if datetime.utcnow() - user.last_login > timedelta(days=92):
            user.is_active = False
