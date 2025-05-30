from rest_framework import serializers
from authentication.models import User


class MeSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "permissions"]

    def get_permissions(self, user):
        return list(user.get_all_permissions())
