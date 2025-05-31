from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from data_mapping.models import DataSubjectType
from data_mapping.serializers.data_subject_type import DataSubjectTypeSerializer


class DataSubjectTypeViewSet(viewsets.ModelViewSet):
    queryset = DataSubjectType.objects.all()
    serializer_class = DataSubjectTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(deleted_at__isnull=True)
