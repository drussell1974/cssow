from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="topic.index"),
    path('delete_unpublished', views.index, name="topic.delete_unpublished"),  # TODO: implement delete_unpublished
    path('new', views.edit, name="topic.new"),
    path('<int:topic_id>/edit', views.edit, name="topic.edit")
]