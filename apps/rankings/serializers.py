from rest_framework import serializers


class TopUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    total_score = serializers.IntegerField()
    position = serializers.IntegerField()

class UserPositionSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    total_score = serializers.IntegerField()
