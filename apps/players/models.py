from django.db import models
from apps.core.models import CreateModifiedDateTimeBase
from apps.tournaments.models import TournamentPlayingCategory

# Create your models here.


class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country_name


class Players(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    country_code = models.ForeignKey("players.Country", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Players"


class PlayingIn(models.Model):
    registration_id = models.ForeignKey(
        "players.Registration", on_delete=models.CASCADE
    )
    seed = models.IntegerField()
    tournament_playing_category = models.ForeignKey(
        "tournaments.TournamentPlayingCategory", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Playing In"


class Registration(models.Model):
    registration_date = models.DateField()

    class Meta:
        verbose_name_plural = "Registration"


class RegistrationPlayer(models.Model):
    registration = models.ForeignKey("players.Registration", on_delete=models.CASCADE)
    player_id = models.ForeignKey("players.Players", on_delete=models.CASCADE)
