from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from apps.ai_features.services import detect_toxic_text


class ChatRoomViewSet(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filterset_fields = ("room", "sender", "is_seen")

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content", "")
        moderation = detect_toxic_text(content)
        if moderation.is_toxic:
            content = "[Message removed by moderation]"
        serializer.save(sender=self.request.user, content=content)

    @action(detail=True, methods=["post"], url_path="mark-seen")
    def mark_seen(self, request, pk=None):
        message = self.get_object()
        message.is_seen = True
        message.save(update_fields=["is_seen"])
        return Response({"detail": "Message marked as seen"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="edit")
    def edit(self, request, pk=None):
        message = self.get_object()
        if message.sender_id != request.user.id:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        message.content = request.data.get("content", message.content)
        message.edited_at = timezone.now()
        message.save(update_fields=["content", "edited_at"])
        return Response(MessageSerializer(message).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="delete")
    def soft_delete(self, request, pk=None):
        message = self.get_object()
        if message.sender_id != request.user.id:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        message.is_deleted = True
        message.save(update_fields=["is_deleted"])
        return Response({"detail": "Message deleted"}, status=status.HTTP_200_OK)
