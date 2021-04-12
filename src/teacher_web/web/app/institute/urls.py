from django.urls import include, path

from . import views

urlpatterns = [
    
    path('all', views.all, name='institute.all'),
    path('new', views.edit, name='institute.new'),
    path('delete_unpublished', views.delete_unpublished, name="institute.delete_unpublished"),
    path('<int:institute_id>', views.index, name='institute.view'),
    path('<int:institute_id>/schedule', views.schedule, name="institute.schedule"),
    path('<int:institute_id>/edit', views.edit, name='institute.edit'),
    path('<int:institute_id>/publish', views.index, name='institute.publish_item'),
    #path('<int:institute_id>/delete', views.index, name='institute.delete'),
    path('<int:institute_id>/department/', include('app.department.urls')),
    path('<int:institute_id>/academic-years/', include('app.academic_years.urls')),
    path('', views.index, name='institute.index'), 
]