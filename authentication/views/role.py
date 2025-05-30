from rest_framework import viewsets
from authentication.models import Role
from authentication.serializers import RoleSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsSuperuser, IsAdmin


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsSuperuser | IsAdmin]
