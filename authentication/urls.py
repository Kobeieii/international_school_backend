from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authentication import views

router = routers.DefaultRouter()
router.register(r'users', views.UserRoleViewSet, basename='user-roles')
router.register(r'permissions', views.PermissionViewSet, basename='permissions')
router.register(r'roles', views.RoleViewSet, basename='roles')

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
