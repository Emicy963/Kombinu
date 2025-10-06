from rest_framework import serializers
from .models import Option, Question, Quiz, QuizSubmission


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("pk", "text")
        read_only_fields = ("pk",)


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("pk", "question_text", "options")
        read_only_fields = ("pk",)


class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ("pk", "title", "content", "questions")
        read_only_fields = ("pk", "title", "content", "questions")


class QuizAnswerSubmissionSerializer(serializers.Serializer):
    question_id = serializers.UUIDField()
    selected_option_id = serializers.UUIDField()


class QuizSubmissionSerializer(serializers.Serializer):
    answers = QuizAnswerSubmissionSerializer(many=True)

    def validate(self, data):
        if not data.get('answers'):
            raise serializers.ValidationError("At least one answer is required.")
        return data


class QuizGenerationSerializer(serializers.Serializer):
    difficulty = serializers.ChoiceField(
        choices=["easy", "medium", "hard"], required=False
    )
    number_of_questions = serializers.IntegerField(  # CORRIGIDO: era number_of_question
        min_value=1, max_value=50, required=False, default=10
    )
