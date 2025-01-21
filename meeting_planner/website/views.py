from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                           {"meetings": Meeting.objects.all()})

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page")

def about(request):
    return HttpResponse("Everything about me..!!!!")