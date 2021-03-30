from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.select, name="lesson_ks123pathways.index"),
    # TODO: create index to replace above - path('', views.select, name="lesson_pathways.select"),
    #path('delete_unpublished', views.delete_unpublished, name="lesson_pathways.delete_unpublished"), 
    path('select', views.select, name="lesson_ks123pathways.select"),
    #path('new', views.new, name="lesson_pathways.new"),
    #path('<int:pathway_item_id>/edit', views.edit, name="lesson_pathways.edit"),
    #path('<int:pathway_item_id>/delete', views.delete_item, name="lesson_pathways.delete_item"), 
    #path('<int:pathway_item_id>/publish_item', views.publish_item, name="lesson_pathways.publish_item"), 
    #path('<int:pathway_item_id>/save', views.save, name="lesson_pathways.save")
]