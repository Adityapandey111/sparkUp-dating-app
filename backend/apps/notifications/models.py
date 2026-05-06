from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class Notification(UUIDPrimaryKeyModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    notification_type = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    metadata = models.JSONField(default=dict, blank=True)
    is_read = models.BooleanField(default=False)
