from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='learningobjective.index'),
    path('<int:learning_objective_id>/delete', views.index, name='learningobjective.delete_item'),
    path('<int:learning_objective_id>/edit', views.index, name='learningobjective.edit'),
]