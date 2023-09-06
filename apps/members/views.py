from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Members

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


class HomePage(TemplateView):
    template_name = "home_page.html"
