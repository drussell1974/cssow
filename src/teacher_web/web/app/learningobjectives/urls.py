from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='learningobjective.index'),
    path('new', views.new, name='learningobjective.new'),
    path('delete_unpublished', views.delete_unpublished, name='learningobjective.delete_unpublished'),
    path('<int:learning_objective_id>/edit', views.edit, name='learningobjective.edit'),
    path('<int:learning_objective_id>/save', views.save, name='learningobjective.save'),
    path('<int:learning_objective_id>/publish', views.publish_item, name="learningobjective.publish_item"),
    path('<int:learning_objective_id>/delete', views.delete_item, name='learningobjective.delete_item'),
]