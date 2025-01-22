from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    # This will ensure to query the database to retrieve all the objects only if the user is successfully authenticated.
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        # If the user is not valid, then the database call is prevented.
        context = {}

    return render(request, "website/welcome.html", context)


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page")


def about(request):
    return HttpResponse("Everything about me..!!!!")
