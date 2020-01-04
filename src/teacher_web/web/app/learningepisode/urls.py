from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="learningepisode.index"),
    path('new', views.new, name="learningepisode.new"),
    path('<int:learning_episode_id>', views.index, name="learningepisode.view"),
    path('<int:learning_episode_id>/edit', views.edit, name="learningepisode.edit"),
    path('<int:learning_episode_id>/copy', views.copy, name="learningepisode.copy"), 
    path('<int:learning_episode_id>/publish', views.publish, name="learningepisode.publish_item"), 
    path('<int:learning_episode_id>/delete', views.delete, name="learningepisode.delete_item"), 
    path('<int:learning_episode_id>/lessonplan', views.lessonplan, name="learningepisode.lessonplan"),
    path('<int:learning_episode_id>/whiteboard', views.whiteboard, name="learningepisode.whiteboard_view"),
    # Check learningobjective app
    path('<int:learning_episode_id>/learningobjectives/', include('app.learningobjectives.urls')),
]