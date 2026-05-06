from rest_framework import serializers
from .models import Swipe, Match


class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = "__all__"
        read_only_fields = ("id", "user")


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"
