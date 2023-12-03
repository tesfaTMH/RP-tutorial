from django.db.models.signals import post_save # signal that needs to be fired 
from django.contrib.auth.models import User     # user model acts as sender

# we also need a receiver that accepts the signal to perform a task
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()