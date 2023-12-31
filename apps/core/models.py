from django.db import models


class CreateModifiedDateTimeBase(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
