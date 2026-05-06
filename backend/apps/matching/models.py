from django.conf import settings
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class SwipeType(models.TextChoices):
    LIKE = "like", "Like"
    PASS = "pass", "Pass"
    SUPER = "super", "Super Like"


class Swipe(UUIDPrimaryKeyModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="swipes")
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="swiped_by")
    swipe_type = models.CharField(max_length=10, choices=SwipeType.choices)

    class Meta:
        unique_together = ("user", "target")


class Match(UUIDPrimaryKeyModel, TimeStampedModel):
    user_one = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="matches_initiated")
    user_two = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="matches_received")
    compatibility_score = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
