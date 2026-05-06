from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel, SoftDeleteModel


class Post(UUIDPrimaryKeyModel, TimeStampedModel, SoftDeleteModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    caption = models.TextField(blank=True)
    media_url = models.URLField(blank=True)
    media_type = models.CharField(max_length=20, default="image")
    hashtags = models.JSONField(default=list, blank=True)
    mentions = models.JSONField(default=list, blank=True)
