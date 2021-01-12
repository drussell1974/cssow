from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="eventlog.index"),
    path("", views.index, name="eventlog.index"),
    path("delete", views.delete, name="eventlog.delete")
]