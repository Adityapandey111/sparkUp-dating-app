from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import timedelta
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


def default_story_expiry():
    return timezone.now() + timedelta(hours=24)


class Story(UUIDPrimaryKeyModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="stories")
    media_url = models.URLField()
    caption = models.CharField(max_length=255, blank=True)
    expires_at = models.DateTimeField(default=default_story_expiry)
