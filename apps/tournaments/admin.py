from django.contrib import admin
from apps.tournaments import models

# Register your models here.


class CustomTournamentType(admin.ModelAdmin):
    list_display = ("tournament_type",)


class CustomTournaments(admin.ModelAdmin):
    list_display = (
        "tournament_name",
        "location",
        "start_date",
        "end_date",
        "numbers_of_rounds",
        "tournament_type_id",
    )


class CustomPlayingCategory(admin.ModelAdmin):
    list_display = ("category_name",)


class CustomTournamentPlayingCategory(admin.ModelAdmin):
    list_display = ("tournament_id", "playing_category")


admin.site.register(models.TournamentType, CustomTournamentType)
admin.site.register(models.Tournaments, CustomTournaments)
admin.site.register(models.PlayingCategory)
admin.site.register(models.TournamentPlayingCategory)
