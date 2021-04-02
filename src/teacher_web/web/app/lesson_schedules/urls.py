from django.urls import include, path

from . import views

urlpatterns = [
    #path('', views.index, name="lesson.index"),
    path('new', views.edit, name="lesson_schedule.new")
    #path('<int:lesson_id>/edit', views.edit, name="lesson.edit"),
    #path('<int:lesson_id>/copy', views.edit, { "is_copy": True }, name="lesson.copy"), 
    #path('<int:lesson_id>/whiteboard', views.whiteboard, name="lesson.whiteboard_view"),
    #path('<int:lesson_id>/learning-objectives/missing-words', views.missing_words_challenge, name="lesson.missing_words_challenge_view"),
]