from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="lesson_keywords.index"),
    path('delete_unpublished', views.delete_unpublished, name="lesson_keywords.delete_unpublished"), 
    path('select', views.select, name="lesson_keywords.select"),
    path('new', views.new, name="lesson_keywords.new"),
    path('<int:keyword_id>/edit', views.edit, name="lesson_keywords.edit"),
    path('<int:keyword_id>/delete', views.delete_item, name="lesson_keywords.delete_item"), 
    path('<int:keyword_id>/publish_item', views.publish_item, name="lesson_keywords.publish_item"), 
    path('<int:keyword_id>/save', views.save, name="lesson_keywords.save")
]