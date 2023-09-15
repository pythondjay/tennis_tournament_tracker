from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
]
