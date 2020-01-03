from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="learningepisode.index"),
    path('new', views.new, name="learningepisode.new"),
    path('<int:learning_episode_id>', views.index, name="learningepisode.view"),
    # Check learningobjective app
    path('<int:learning_episode_id>/learningobjectives/', include('app.learningobjectives.urls')),
]