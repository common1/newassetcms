from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class BaseModel(models.Model):
    created_by = UserForeignKey(
        auto_user_add=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = UserForeignKey(
        auto_user=True,
        auto_user_add=True,
        related_name="%(app_label)ss_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss"
    )
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
