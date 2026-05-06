from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel, SoftDeleteModel


class Profile(UUIDPrimaryKeyModel, TimeStampedModel, SoftDeleteModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=20, blank=True)
    interested_in = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=120, blank=True)
    profession = models.CharField(max_length=120, blank=True)
    education = models.CharField(max_length=120, blank=True)
    height_cm = models.PositiveSmallIntegerField(null=True, blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    profile_video_url = models.URLField(blank=True)
    voice_intro_url = models.URLField(blank=True)
    interests = models.JSONField(default=list, blank=True)
    personality_type = models.CharField(max_length=12, blank=True)
    relationship_preference = models.CharField(max_length=120, blank=True)
    languages = models.JSONField(default=list, blank=True)
    lifestyle_preferences = models.JSONField(default=dict, blank=True)
    profile_completion = models.PositiveSmallIntegerField(default=10)
    is_hidden = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
