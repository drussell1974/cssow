from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="ks123pathways.index"),
    path('delete_unpublished', views.delete_unpublished, name="ks123pathways.delete_unpublished"), 
    path('new', views.edit, name="ks123pathways.new"),
    path('<int:pathway_item_id>/edit', views.edit, name="ks123pathways.edit")
]