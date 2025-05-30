from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from authentication.models.role import Role


class CustomUserManager(BaseUserManager):

    def is_valid_email(self, email):
        try:
            email, domain_part = email.strip().rsplit("@", 1)
            if not domain_part:
                return False
            return True
        except ValueError:
            return False

    def create_user(self, email, password=None, **extra_fields):
        if not email or not self.is_valid_email(email):
            raise ValueError("Email must be valid")
        if not password:
            raise ValueError("Password must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField(Role, related_name="users")
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_all_permissions(self):
        perms = set()
        for role in self.roles.prefetch_related("permissions", "parents__permissions"):
            perms.update(role.get_all_permissions())
        return set(p.code for p in perms)
