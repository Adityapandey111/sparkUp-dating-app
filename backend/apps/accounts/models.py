from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models import UUIDPrimaryKeyModel, TimeStampedModel


class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    MODERATOR = "moderator", "Moderator"
    USER = "user", "User"
    VERIFIED = "verified", "Verified User"


class User(UUIDPrimaryKeyModel, AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    is_email_verified = models.BooleanField(default=False)
    last_active = models.DateTimeField(null=True, blank=True)
    blocked_users = models.ManyToManyField("self", symmetrical=False, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.email
