from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
    path("login/", views.user_login, name="user-login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
]
