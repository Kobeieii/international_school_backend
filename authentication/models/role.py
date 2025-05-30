from django.db import models
from authentication.models.permission import Permission


class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission)
    parents = models.ManyToManyField("self", symmetrical=False, blank=True)
