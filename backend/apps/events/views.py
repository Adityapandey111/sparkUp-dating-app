from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_fields = ("location",)
    ordering_fields = ("starts_at", "created_at")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
