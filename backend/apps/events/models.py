from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class Event(UUIDPrimaryKeyModel, TimeStampedModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_events")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=180)
    starts_at = models.DateTimeField()
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events", blank=True)
