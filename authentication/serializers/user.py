from rest_framework import serializers
from authentication.models import User, Role
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "roles"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        roles = validated_data.pop("roles", [])

        with transaction.atomic():
            user = User(**validated_data)
            if password:
                user.set_password(password)
            user.save()
            user.roles.set(roles)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        roles = validated_data.pop("roles", [])

        with transaction.atomic():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            if roles:
                instance.roles.set(roles)
            else:
                instance.roles.clear()
        return instance
