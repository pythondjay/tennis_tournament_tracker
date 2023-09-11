from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Tournaments
from .form import TournamentsForm
from apps.members.views import home_page

# Create your views here.


def tournament_info(request, id):
    tournament = Tournaments.objects.get(pk=id)

    context = {
        "tournament": tournament,
    }

    return render(request, "tournaments/tournament_info.html", context)


def tournament_info_form(request):
    if request.POST:
        form = TournamentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home_page)
    return render(
        request, "tournaments/tournament_info_form.html", {"form": TournamentsForm}
    )
