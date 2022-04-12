from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.dispatch import receiver # Import the receiver
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    send_mail('Login', f'{request.user.username} login',
              settings.EMAIL_HOST_USER,
              ['lesobrod@yandex.ru'],
              fail_silently=False)

    send_mail('Привет!', 'Любви и добра!',
              settings.EMAIL_HOST_USER,
              ['anahata-irina@yandex.ru'],
              fail_silently=False)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    send_mail('Logout', f'{request.user.username} logout',
              settings.EMAIL_HOST_USER,
              ['lesobrod@yandex.ru'],
              fail_silently=False)