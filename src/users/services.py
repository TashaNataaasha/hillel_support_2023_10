from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User, ActivationKey

@receiver(post_save, sender=User)
def create_activation_key(sender, instance, created, **kwargs):
    if created:
        activation_key = ActivationKey.objects.create(user=instance)
        activation_key.save()
        send_mail(
            'Please activate your account',
            f'Please activate your account: {activation_key.key}',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )