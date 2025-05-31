from rest_framework import serializers
from data_mapping.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "deleted_at"]
