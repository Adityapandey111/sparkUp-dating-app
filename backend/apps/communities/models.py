from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class Community(UUIDPrimaryKeyModel, TimeStampedModel):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="communities", blank=True)
