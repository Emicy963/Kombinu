from rest_framework import serializers


class CreatorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        from accounts.models import CustomUser
        model = CustomUser
        fields = ("id", "name")
    
    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.email
