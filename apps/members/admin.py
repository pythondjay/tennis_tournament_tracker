from django.contrib import admin
from apps.members import models


# Register your models here.
class CustomMembers(admin.ModelAdmin):
    list_display = (
        "id",
        "firstname",
        "lastname",
        "age",
        "email",
        "phone",
        "ability",
        "league",
    )


admin.site.register(models.Members, CustomMembers)
