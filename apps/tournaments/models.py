from django.db import models
from apps.core.models import CreateModifiedDateTimeBase

# Create your models here.


class TournamentType(models.Model):
    tournament_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tournament Type"

    def __str__(self):
        return self.tournament_type


class Tournaments(models.Model):
    tournament_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    numbers_of_rounds = models.IntegerField(null=True, blank=True)
    tournament_type_id = models.ForeignKey(
        "tournaments.TournamentType", on_delete=models.CASCADE
    )
    surface = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tournaments"

    def __str__(self):
        return str(self.tournament_type_id)


class PlayingCategory(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Playing Category"

    def __str__(self):
        return f"{self.category_name}"


class TournamentPlayingCategory(models.Model):
    tournament_id = models.ForeignKey(
        "tournaments.Tournaments", on_delete=models.CASCADE
    )
    playing_category = models.ForeignKey(
        "tournaments.PlayingCategory", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Tournament Playing Category"
