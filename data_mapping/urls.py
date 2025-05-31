from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data_mapping import views

router = DefaultRouter()
router.register(
    r"data-subject-types", views.DataSubjectTypeViewSet, basename="data-subject-type"
)
router.register(r"departments", views.DepartmentViewSet, basename="department")
router.register(r"titles", views.TitleViewSet, basename="title")
urlpatterns = [
    path("", include(router.urls)),
]
