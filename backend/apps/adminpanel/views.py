from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.common.permissions import IsAdminOrModerator
from apps.accounts.models import User
from apps.posts.models import Post
from apps.events.models import Event


class AdminStatsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrModerator]

    def get(self, request):
        return Response(
            {
                "users": User.objects.count(),
                "verified_users": User.objects.filter(is_email_verified=True).count(),
                "posts": Post.objects.count(),
                "events": Event.objects.count(),
            }
        )
