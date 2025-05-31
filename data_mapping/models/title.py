from django.db import models
from data_mapping.models.department import Department
from data_mapping.models.data_subject_type import DataSubjectType
from django.utils import timezone


class Title(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="titles"
    )
    data_subject_types = models.ManyToManyField(
        DataSubjectType,
        related_name="titles",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
