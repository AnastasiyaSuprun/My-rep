from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .mixins import SoftDateTimeMixin


class Owner(SoftDateTimeMixin):

    class Meta(type):
        verbose_name = u'pet owner'
        verbose_name_plural = u'pet owners'
        ordering = ['first_name', 'last_name']

    first_name = models.CharField(
        max_length=100,
        blank=False,
    )

    last_name = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    city = models.CharField(
        max_length=20,
        blank=False,
        db_index=True,
    )

    purpose = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(SoftDateTimeMixin):

    class Meta(type):
        verbose_name = u'pet'
        verbose_name_plural = u'pets'
        ordering = ['breed']

    breed = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    nickname = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    age = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        blank=False,
    )

    sex = models.CharField(
        max_length=1,
        blank=False,
    )

    owner = models.ForeignKey(
        Owner,
        max_length=100,
        blank=False,
        on_delete=models.PROTECT
    )

    photo = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.breed} {self.nickname} is looking for a friend.'


class Shelter(SoftDateTimeMixin):

    class Meta(type):
        verbose_name = u'shelter'
        verbose_name_plural = u'shelters'
        ordering = ['title']

    title = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    manager = models.CharField(
        max_length=100,
        blank=False,
    )

    city = models.CharField(
        max_length=20,
        blank=False,
        db_index=True,
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f'{self.title} in {self.city}'


class PetInShelter(SoftDateTimeMixin):

    class Meta(type):
        verbose_name = u'pet'
        verbose_name_plural = u'pets in shelters'
        ordering = ['breed']

    breed = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    nickname = models.CharField(
        max_length=100,
        blank=False,
        db_index=True,
    )

    sex = models.CharField(
        max_length=1,
        blank=False,
    )

    shelter_field = models.ForeignKey(
        Shelter,
        max_length=100,
        blank=False,
        on_delete=models.PROTECT
    )

    photo = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.breed} {self.nickname} is looking for a family.'
