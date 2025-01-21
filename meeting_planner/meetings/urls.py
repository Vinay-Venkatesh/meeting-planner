from django.urls import path
from meetings import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"), # <int:id> - an integer needs to be passed whose name is id (here id is the view parameter)
    path('rooms', views.room, name="rooms"), # name is used to refer this path in website app
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]