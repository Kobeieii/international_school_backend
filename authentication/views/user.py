from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsSuperuser, IsAdmin


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperuser | IsAdmin]
