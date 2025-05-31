from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from data_mapping.models import Department
from data_mapping.serializers.department import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(deleted_at__isnull=True)
