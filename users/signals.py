from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
	request_sender= instance.request_sender
	request_receiver = instance.request_receiver

	if instance.status =="accepted":
		request_sender.friends.add(request_receiver.user)
		request_receiver.friends.add(request_sender.user)
		request_sender.save()
		request_receiver.save()
