from django.core import signing
from django.conf import settings


class AccountTokenService:
    EMAIL_VERIFICATION_SALT = "sparkup-email-verify"
    RESET_PASSWORD_SALT = "sparkup-reset-password"
    MAX_AGE_SECONDS = 60 * 60 * 24

    @classmethod
    def make_email_token(cls, user_id: str) -> str:
        return signing.dumps({"uid": str(user_id)}, salt=cls.EMAIL_VERIFICATION_SALT)

    @classmethod
    def read_email_token(cls, token: str) -> str:
        data = signing.loads(token, salt=cls.EMAIL_VERIFICATION_SALT, max_age=cls.MAX_AGE_SECONDS)
        return data["uid"]

    @classmethod
    def make_reset_token(cls, user_id: str) -> str:
        return signing.dumps({"uid": str(user_id)}, salt=cls.RESET_PASSWORD_SALT, key=settings.SECRET_KEY)

    @classmethod
    def read_reset_token(cls, token: str) -> str:
        data = signing.loads(
            token,
            salt=cls.RESET_PASSWORD_SALT,
            max_age=cls.MAX_AGE_SECONDS,
            key=settings.SECRET_KEY,
        )
        return data["uid"]
