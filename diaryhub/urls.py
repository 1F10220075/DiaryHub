from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.diary, name="diary"),
    path("create", views.create, name="create"),
    path("<int:id>/delete", views.delete, name="delete"),
]