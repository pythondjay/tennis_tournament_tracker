from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("members/<int:id>", views.members_info, name="members-info"),
]
