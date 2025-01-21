from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from meetings.models import Meeting, Room


def detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id) # Takes in model name and the input parameter to check in database
    return render(request, "meetings/meeting_details.html", {"meeting": meeting})

def room(request):
    rooms = Room.objects.all()
    return render(request, "meetings/room_details.html", {"rooms":rooms})

# Generates form based on the meeting model class objects
MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST) # passing the request object to modelform_factory
        if form.is_valid(): # server validation for form inputs
            form.save()
            return redirect("home") # redirects to welcome page
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form":form})

def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting) # passing the request object to modelform_factory along with the meeting object instance that needs to be edited
        if form.is_valid(): # server validation for form inputs
            form.save()
            return redirect("detail",id) # redirects to respective details page
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", {"form":form})

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("home")
    else:
        return render(request, "meetings/confirm_delete.html", {"meeting":meeting})
