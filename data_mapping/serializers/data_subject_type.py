from rest_framework import serializers
from data_mapping.models import DataSubjectType


class DataSubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSubjectType
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "deleted_at"]
