from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from data_mapping.models import Title, Department, DataSubjectType
from data_mapping.serializers.title import TitleSerializer, TitleExcelSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.prefetch_related("department", "data_subject_types").all()
    serializer_class = TitleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(deleted_at__isnull=True)

    @action(detail=False, methods=["post"], url_path="import-excel")
    def import_excel(self, request):
        req_data = request.data
        serializer = TitleExcelSerializer(data=req_data, many=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        department_map = {dept.name: dept.id for dept in Department.objects.all()}
        data_subject_types_map = {
            ds_type.name: ds_type.id for ds_type in DataSubjectType.objects.all()
        }

        try:
            with transaction.atomic():
                for data in serializer.validated_data:
                    department_id = department_map.get(data.get("department"))
                    if not department_id:
                        raise ValueError(f"Invalid department: {data.get('department')}")

                    data_subject_type_ids = [
                        data_subject_types_map[ds_type.strip()]
                        for ds_type in data.get("data_subject_types", "").split(",")
                        if ds_type.strip() in data_subject_types_map
                    ]

                    title = Title.objects.create(
                        name=data.get("title"),
                        description=data.get("description", ""),
                        department_id=department_id,
                    )
                    title.data_subject_types.set(data_subject_type_ids)

            return Response({"detail": "Import successful"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"detail": f"Import failed: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )