from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="department_topic.index"),
    path('delete_unpublished', views.delete_unpublished, name="department_topic.delete_unpublished"),  # TODO: implement delete_unpublished
    path('new', views.edit, name="department_topic.new"),
    path('<int:topic_id>/edit', views.edit, name="department_topic.edit")
]