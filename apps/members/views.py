from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Members
from .form import MembersForm


# Create your views here.


def home_page(request):
    member_cnt = Members.objects.all().count()

    context = {
        "member_cnt": member_cnt,
    }

    return render(
        request,
        "members/home.html",
        context,
    )


def members_info(request, id):
    mem = Members.objects.get(pk=id)

    context = {
        "mem": mem,
    }

    return render(
        request,
        "members/members_info.html",
        context,
    )


def members_info_form(request):
    if request.POST:
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home_page)
    return render(request, "members/members_info_form.html", {"form": MembersForm})


class HomePage(TemplateView):
    template_name = "home_page.html"
