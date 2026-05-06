from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class ChatRoom(UUIDPrimaryKeyModel, TimeStampedModel):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="chat_rooms")
    is_group = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True)


class Message(UUIDPrimaryKeyModel, TimeStampedModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField(blank=True)
    message_type = models.CharField(max_length=20, default="text")
    is_seen = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="replies")
    media_url = models.URLField(blank=True)
