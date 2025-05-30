from rest_framework import viewsets
from authentication.models import Permission
from authentication.serializers import PermissionSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsSuperuser, IsAdmin


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser | IsAdmin]
