from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="lesson_schedule.index"),
    path('new', views.edit, name="lesson_schedule.new"),
    path('<int:schedule_id>/edit', views.edit, name="lesson_schedule.edit"),
    path('<int:schedule_id>/delete', views.delete, name="lesson_schedule.delete"),
    path('<int:schedule_id>/whiteboard', views.whiteboard, name="lesson_schedule.whiteboard_view"),
]