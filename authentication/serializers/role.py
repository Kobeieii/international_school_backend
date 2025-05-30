from rest_framework import serializers
from authentication.models import Role, Permission


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(), many=True
    )
    parents = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), many=True, required=False
    )

    class Meta:
        model = Role
        fields = ["id", "name", "permissions", "parents"]
