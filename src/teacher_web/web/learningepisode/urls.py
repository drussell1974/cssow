from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="lessons"),
    path('<int:learning_episode_id>', views.index, name="lesson")
]