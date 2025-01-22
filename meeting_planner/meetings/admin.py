from django.contrib import admin
from django.contrib.admin import ModelAdmin

from meetings.models import Meeting, Room

# To register the Model to admin site.
admin.site.register(Room)

# admin.site.register(Meeting)

# To customize the meetings section in the admin page

@admin.register(Meeting)
class MeetingAdmin(ModelAdmin):
    model = Meeting
    list_display = ("id", "title", "date", "start_time", "room") # table cols
    ordering = ("date", "start_time") # order by start_time of the meeting
    search_fields = ("title",) # search by meeting title

