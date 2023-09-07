from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tournaments

# Create your views here.


def tournament_info(request, id):
    tournament = Tournaments.objects.get(pk=id)

    context = {
        "tournament": tournament,
    }

    return render(
        request,
        "tournaments/tournament_info.html",
        context,
    )
