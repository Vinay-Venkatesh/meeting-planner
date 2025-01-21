from django.contrib import admin

from meetings.models import Meeting, Room

# To register the Model to admin site.
admin.site.register(Meeting)
admin.site.register(Room)
