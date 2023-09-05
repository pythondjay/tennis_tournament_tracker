from django.db import models
from apps.core.models import CreateModifiedDateTimeBase

# Create your models here.


class FixtureResults(models.Model):
    fixture_id = models.ForeignKey(
        "results.Fixture",
        on_delete=models.CASCADE,
    )
    winners_name = models.CharField(max_length=255)
    runner_up_name = models.CharField(max_length=255)
    is_opponent_retired = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "Results"


class Fixture(models.Model):
    tournament_playing_category = models.ForeignKey(
        "tournaments.TournamentPlayingCategory", on_delete=models.CASCADE
    )
    first_player = models.CharField(max_length=255)
    second_player = models.CharField(max_length=255)
    round = models.IntegerField()


class SetScore(models.Model):
    fixture_id = models.ForeignKey(
        "results.Fixture",
        on_delete=models.CASCADE,
    )
    set_number = models.IntegerField()
    first_registration_games = models.IntegerField()
    second_registration_games = models.IntegerField()

    class Meta:
        verbose_name_plural = "Set Scores"


class GameScore(models.Model):
    fixture_id = models.ForeignKey(
        "results.Fixture",
        on_delete=models.CASCADE,
    )
    set_number = models.IntegerField()
    game_number = models.IntegerField()
    first_registration_point = models.IntegerField()
    second_registration_point = models.IntegerField()

    class Meta:
        verbose_name_plural = "Game Scores"


class TieBreaker(models.Model):
    fixture_id = models.ForeignKey(
        "results.Fixture",
        on_delete=models.CASCADE,
    )
    set_number = models.IntegerField()
    first_registration_breaker = models.IntegerField()
    second_registration_breaker = models.IntegerField()

    class Meta:
        verbose_name_plural = "Tie Breaks"
