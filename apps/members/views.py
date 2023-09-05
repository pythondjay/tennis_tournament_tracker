from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Members

# Create your views here.


def home_page(request):
    member_cnt = Members.objects.all().count()

    response = f"""
    <html>
    
    <h1>Welcome to TennisTracker</h1>
    
    <p> {member_cnt} active users and counting </p>
    
    </html>
    
    """

    return HttpResponse(response)


def members_info(request, id):
    mem = Members.objects.get(pk=id)

    response = f"""
    <html>
        <h1>Tennis Club Members</h1>
        <p><b>First Name</b>: {mem.firstname}</p>
        <p><b>Surname</b>: {mem.lastname}</p>
        <p><b>Age</b>: {mem.age}</p>
        <p><b>Email address</b>: {mem.email}</p>
        <p><b>Phone Number</b>: {mem.phone}</p>
        <p><b>Ability</b>: {mem.ability}</p>
        <p><b>League</b>: {mem.league}</p>       
    </html>
    """

    return HttpResponse(response)


class HomePage(TemplateView):
    template_name = "home_page.html"
