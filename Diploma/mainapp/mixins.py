from django.db import models
from django.utils import timezone


class SoftDateTimeMixin(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=True,
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
