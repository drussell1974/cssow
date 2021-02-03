from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="content.index"),
    path('delete_unpublished', views.delete_unpublished, name="content.delete_unpublished"), 
    path('new', views.edit, name="content.new"),
    path('<int:content_id>/edit', views.edit, name="content.edit"),
]