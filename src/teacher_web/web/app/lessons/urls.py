from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="lesson.index"),
    path('initialise_keywords', views.initialise_keywords, name="lesson.initialise_keywords"),
    path('delete_unpublished', views.delete_unpublished, name="lesson.delete_unpublished"), 
    path('new', views.new, name="lesson.new"),
    path('<int:lesson_id>', views.index, name="lesson.view"),
    path('<int:lesson_id>/edit', views.edit, name="lesson.edit"),
    path('<int:lesson_id>/copy', views.copy, name="lesson.copy"), 
    path('<int:lesson_id>/publish', views.publish, name="lesson.publish_item"), 
    #path('<int:lesson_id>/delete', views.delete, name="lesson.delete"), 
    path('<int:lesson_id>/lessonplan', views.lessonplan, name="lesson.lessonplan"),
    path('<int:lesson_id>/whiteboard', views.whiteboard, name="lesson.whiteboard_view"),
    path('<int:lesson_id>/save', views.save, name="lesson.save"),
    # Check learningobjective app
    path('<int:lesson_id>/learning-objectives/', include('app.learningobjectives.urls')),
    path('<int:lesson_id>/resources/', include('app.resources.urls')),
]