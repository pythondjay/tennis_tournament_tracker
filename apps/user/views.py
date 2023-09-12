from django.shortcuts import render, redirect
from .models import User
from apps.members.views import home_page
from .form import UserLogin

# Create your views here.


def user_list(request):
    users = User.objects.all()

    context = {
        "users": users,
    }

    return render(request, "user/user_list.html", context)


def user_login(request):
    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home_page)
    return render(request, "user/user_login.html", {"form": UserLogin})
