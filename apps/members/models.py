from django.db import models
from apps.core.models import CreateModifiedDateTimeBase

# Create your models here.


class Members(CreateModifiedDateTimeBase):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    ability = models.CharField(max_length=100)
    league = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name_plural = "Members"
