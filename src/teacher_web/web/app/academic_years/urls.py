from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='academic-year.index'),
    path('new', views.edit, name='academic-year.new'),
    #path('delete_unpublished', views.delete_unpublished, name="department.delete_unpublished"),
    path('<int:year>/edit', views.edit, name='academic-year.edit'),
    #path('<int:department_id>/publish', views.publish, name='department.publish_item'),
    path('change', views.change, name="default.academic-year")
]