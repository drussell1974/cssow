from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="resource.index"),
    path('delete_unpublished', views.delete_unpublished, name="resource.delete_unpublished"), 
    path('new', views.new, name="resource.new"),
    path('<int:resource_id>/edit', views.edit, name="resource.edit"),
    path('<int:resource_id>/delete', views.delete_item, name="resource.delete_item"), 
    path('<int:resource_id>/publish_item', views.publish_item, name="resource.publish_item"), 
    path('<int:resource_id>/save', views.save, name="resource.save")
]