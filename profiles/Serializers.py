from profiles.models import Score
from rest_framework import serializers


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ("user", "total")
