from django.db import models
from authentication.models.permission import Permission


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, related_name="roles")
    parents = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="children"
    )

    def get_all_permissions(self, visited=None):
        if visited is None:
            visited = set()

        if self.id in visited:
            return set()

        visited.add(self.id)

        perms = set(self.permissions.all())
        for parent in self.parents.all():
            perms.update(parent.get_all_permissions(visited))
        return perms
