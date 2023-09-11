from django.urls import path
from . import views

urlpatterns = [
    path("tournaments/<int:id>", views.tournament_info, name="tournament-info"),
    path("tournaments/info", views.tournament_info_form, name="tournament-info"),
]
