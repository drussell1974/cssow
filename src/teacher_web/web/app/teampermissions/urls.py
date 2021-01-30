from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="team-permissions.index"),
    path('schemeofwork/<int:scheme_of_work_id>/teacher/<int:teacher_id>/edit', views.edit, name='team-permissions.edit'),
    path('schemeofwork/<int:scheme_of_work_id>/teacher/<int:teacher_id>/delete', views.delete, name='team-permissions.delete'),
]
