from uuid import uuid4

from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Owner
from mainapp.models import Pet


@receiver(post_save, sender=Owner, dispatch_uid=uuid4())
def owner_handler(sender, **kwargs):
    print('Save is called!')


@receiver(post_save, sender=Pet, dispatch_uid=uuid4())
def pet_handler(sender, **kwargs):
    print('Save is called!')
