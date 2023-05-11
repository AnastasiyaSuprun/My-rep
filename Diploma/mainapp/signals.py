from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Owner
from mainapp.models import Pet


@receiver(post_save, sender=Owner, dispatch_uid=uuid4())
def create_owner_handler(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(owner=instance)


@receiver(post_save, sender=Pet, dispatch_uid=uuid4())
def create_pet_handler(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(pet=instance)
