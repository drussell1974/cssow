from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="content.index"),
    path('new', views.edit, name="content.new"),
    path('<int:content_id>/edit', views.edit, name="content.edit"),
]