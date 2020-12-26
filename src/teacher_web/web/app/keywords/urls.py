from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="keywords.index"),
    path('delete_unpublished', views.delete_unpublished, name="keywords.delete_unpublished"), 
    path('new', views.new, name="keywords.new"),
    path('<int:keyword_id>/edit', views.edit, name="keywords.edit"),
    path('<int:keyword_id>/delete', views.delete_item, name="keywords.delete_item"), 
    path('<int:keyword_id>/publish_item', views.publish_item, name="keywords.publish_item"), 
    path('<int:keyword_id>/save', views.save, name="keywords.save")
]