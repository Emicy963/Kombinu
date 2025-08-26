from rest_framework import serializers
from .models import Option, Question


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("pk", "text")
        read_only_fields = ("pk")

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("pk", "question_text", "options")
        read_only_fields = ("pk")
