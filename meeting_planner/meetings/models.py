from django.contrib.auth import get_user_model
from django.db import models
from datetime import time


# All django classes should inherit from Parent Model
# Ensure the order of classes are maintained which are being referenced.
# Room class - 1st and then Meeting class ( Room object is referenced in Meeting model)
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.room_name}: room {self.room_number} on floor {self.floor_number}"


class Meeting(models.Model):
    # Attributes of a class
    # Django creates __init__ method for these attributes
    # Creates database column with tile and date with respective datatypes.
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))  # 9am
    duration = models.IntegerField(default=1)  # 1hr
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Room Object reference
    participants = models.ManyToManyField(get_user_model())
    # ManyToManyField - user to meeting mapping (M:M mapping)
    # get_user_model() - returns the user class used - by default it is django.contrib.auth.models.User (Which is added from admin page which is nothing but django used model)

    # This will add human readable info that can be seen in django admin page.
    # Ex: Demo Meeting at 09:00:00 on 2025-01-19
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date} in {self.room.room_name} - floor {self.room.floor_number}"
