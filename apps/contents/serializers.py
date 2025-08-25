from rest_framework import serializers
from contents.models import Content


class CreatorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        from accounts.models import CustomUser
        model = CustomUser
        fields = ("id", "name")
    
    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.email

class ContentSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    has_quiz = serializers.BooleanField(read_only=True)
    quiz_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ("id", "creator", "created_at", "has_quiz", "quiz_id")
