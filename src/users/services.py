from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from .models import User, ActivationKey

@receiver(post_save, sender=User)
def create_activation_key(sender, instance, created, **kwargs):
    if created:
        activation_key = ActivationKey.objects.create(user=instance)
        activation_key.save()
        send_activation_email.delay(instance.email, activation_key.key)

@shared_task
def send_activation_email(email, key):
    send_mail(
        'Please activate your account',
        f'Please activate your account: {key}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )