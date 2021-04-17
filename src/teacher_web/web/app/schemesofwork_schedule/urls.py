from django.urls import include, path

from . import views

urlpatterns = [
    #path('lesson/<int:lesson_id>/new', views.edit, name='schemesofwork_schedule.new'),
    #path('lesson/<int:lesson_id>/<int:schedule_id/edit', views.edit, name='schemesofwork_schedule.edit'),
    path('', views.index, name='schemesofwork_schedule.index'), 
]