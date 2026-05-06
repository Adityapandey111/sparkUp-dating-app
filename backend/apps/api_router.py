from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.accounts.views import AuthViewSet
from apps.profiles.views import ProfileViewSet
from apps.matching.views import SwipeViewSet, MatchViewSet
from apps.chat.views import ChatRoomViewSet, MessageViewSet
from apps.posts.views import PostViewSet
from apps.stories.views import StoryViewSet
from apps.communities.views import CommunityViewSet
from apps.events.views import EventViewSet
from apps.notifications.views import NotificationViewSet

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("profiles", ProfileViewSet, basename="profiles")
router.register("swipes", SwipeViewSet, basename="swipes")
router.register("matches", MatchViewSet, basename="matches")
router.register("chat/rooms", ChatRoomViewSet, basename="chat-rooms")
router.register("chat/messages", MessageViewSet, basename="messages")
router.register("posts", PostViewSet, basename="posts")
router.register("stories", StoryViewSet, basename="stories")
router.register("communities", CommunityViewSet, basename="communities")
router.register("events", EventViewSet, basename="events")
router.register("notifications", NotificationViewSet, basename="notifications")

urlpatterns = [
    path("", include(router.urls)),
]
