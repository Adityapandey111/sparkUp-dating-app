from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
