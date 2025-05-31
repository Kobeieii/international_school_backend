from rest_framework import serializers
from data_mapping.models import Title, Department, DataSubjectType
from data_mapping.serializers.department import DepartmentSerializer
from data_mapping.serializers.data_subject_type import DataSubjectTypeSerializer


class TitleSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        source="department", queryset=Department.objects.all(), write_only=True
    )
    department = DepartmentSerializer(read_only=True)

    data_subject_types_ids = serializers.PrimaryKeyRelatedField(
        source="data_subject_types",
        many=True,
        queryset=DataSubjectType.objects.all(),
        write_only=True,
    )
    data_subject_types = DataSubjectTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "deleted_at"]


class TitleExcelSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255, allow_blank=True)
    department = serializers.CharField(max_length=100)
    data_subject_types = serializers.CharField(max_length=255, allow_blank=True)
