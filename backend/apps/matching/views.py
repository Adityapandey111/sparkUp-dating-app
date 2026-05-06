from rest_framework import viewsets
from .models import Swipe, Match
from .serializers import SwipeSerializer, MatchSerializer


class SwipeViewSet(viewsets.ModelViewSet):
    serializer_class = SwipeSerializer
    queryset = Swipe.objects.all()

    def perform_create(self, serializer):
        swipe = serializer.save(user=self.request.user)
        if swipe.swipe_type in {"like", "super"}:
            reciprocal = Swipe.objects.filter(
                user=swipe.target, target=swipe.user, swipe_type__in=["like", "super"]
            ).exists()
            if reciprocal:
                Match.objects.get_or_create(
                    user_one=min([swipe.user, swipe.target], key=lambda u: str(u.id)),
                    user_two=max([swipe.user, swipe.target], key=lambda u: str(u.id)),
                    defaults={"compatibility_score": 0.72},
                )


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.filter(is_active=True)
