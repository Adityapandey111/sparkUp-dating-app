from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(is_deleted=False)
    filterset_fields = ("gender", "location", "profession", "is_hidden")
    search_fields = ("user__username", "bio", "location", "interests")
    ordering_fields = ("created_at", "updated_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
