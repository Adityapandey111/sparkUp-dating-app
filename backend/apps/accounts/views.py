from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    VerifyEmailSerializer,
)
from .tokens import AccountTokenService
from apps.common.emailing import send_account_email

User = get_user_model()


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class AuthViewSet(viewsets.ViewSet):
    permission_classes = []

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="register")
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AccountTokenService.make_email_token(user.id)
        verify_link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
        send_account_email("Verify your SparkUp email", f"Open this link to verify your email: {verify_link}", user.email)
        refresh = RefreshToken.for_user(user)
        return Response(
            {"user": serializer.data, "refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="login")
    def login(self, request):
        view = LoginView.as_view()
        return view(request._request)

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request):
        token = request.data.get("refresh")
        if token:
            RefreshToken(token).blacklist()
        return Response({"detail": "Logged out."}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="refresh")
    def refresh_token(self, request):
        refresh = request.data.get("refresh")
        token = RefreshToken(refresh)
        return Response({"access": str(token.access_token)}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="verify-email")
    def verify_email(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uid = AccountTokenService.read_email_token(serializer.validated_data["token"])
        user = User.objects.get(id=uid)
        user.is_email_verified = True
        user.save(update_fields=["is_email_verified"])
        return Response({"detail": "Email verified"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="forgot-password")
    def forgot_password(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.validated_data["email"]).first()
        if user:
            token = AccountTokenService.make_reset_token(user.id)
            reset_link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
            send_account_email("SparkUp password reset", f"Use this link to reset password: {reset_link}", user.email)
        return Response({"detail": "If the email exists, reset instructions were sent."}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny], url_path="reset-password")
    def reset_password(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uid = AccountTokenService.read_reset_token(serializer.validated_data["token"])
        user = User.objects.get(id=uid)
        user.set_password(serializer.validated_data["password"])
        user.save(update_fields=["password"])
        return Response({"detail": "Password reset successful"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="block-user")
    def block_user(self, request):
        target = User.objects.get(id=request.data["target_user_id"])
        request.user.blocked_users.add(target)
        return Response({"detail": "User blocked"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="unblock-user")
    def unblock_user(self, request):
        target = User.objects.get(id=request.data["target_user_id"])
        request.user.blocked_users.remove(target)
        return Response({"detail": "User unblocked"}, status=status.HTTP_200_OK)
