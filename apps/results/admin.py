from django.contrib import admin
from apps.results import models

# Register your models here.


class CustomFixtureResults(admin.ModelAdmin):
    list_display = (
        "fixture_id",
        "winners_name",
        "runner_up_name",
        "is_opponent_retired",
    )


class CustomFixture(admin.ModelAdmin):
    list_display = (
        "tournament_playing_category",
        "first_player",
        "second_player",
        "round",
    )


class CustomSetScore(admin.ModelAdmin):
    list_display = (
        "fixture_id",
        "set_number",
        "first_registration_games",
        "second_registration_games",
    )


class CustomGameScore(admin.ModelAdmin):
    list_display = (
        "fixture_id",
        "set_number",
        "game_number",
        "first_registration_point",
        "second_registration_point",
    )


class CustomTieBreaker(admin.ModelAdmin):
    list_display = (
        "fixture_id",
        "set_number",
        "first_registration_breaker",
        "second_registration_breaker",
    )


admin.site.register(models.FixtureResults, CustomFixtureResults)
admin.site.register(models.Fixture, CustomFixture)
admin.site.register(models.SetScore, CustomSetScore)
admin.site.register(models.GameScore, CustomGameScore)
admin.site.register(models.TieBreaker, CustomTieBreaker)
