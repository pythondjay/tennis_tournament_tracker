from django.contrib import admin
from apps.players import models


class CustomCountry(admin.ModelAdmin):
    list_display = ("code", "country_name")


class CustomPlayers(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "country_code",
    )


class CustomPlayingIn(admin.ModelAdmin):
    list_display = ("registration_id", "seed", "tournament_playing_category")


class CustomRegistrationPlayer(admin.ModelAdmin):
    list_display = ("registration", "player_id")


# Register your models here.
admin.site.register(models.Country, CustomCountry)
admin.site.register(models.Players, CustomPlayers)
admin.site.register(models.PlayingIn, CustomPlayingIn)
admin.site.register(models.Registration)
admin.site.register(models.RegistrationPlayer, CustomRegistrationPlayer)
