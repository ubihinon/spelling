from rest_framework import serializers

from apps.cards.models import Answer
from apps.cards.models import LearningSession


class LearningSessionSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(allow_null=True, default=None)

    class Meta:
        model = LearningSession
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(allow_null=True, default=None)

    class Meta:
        model = Answer
        fields = '__all__'
