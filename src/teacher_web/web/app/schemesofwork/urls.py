from django.urls import path

from . import views

urlpatterns = [
    path('new', views.new, name='schemesofwork.new'),
    path('delete_unpublished', views.delete_unpublished, name="schemesofwork.delete_unpublished"),
    path('<int:scheme_of_work_id>', views.index, name='schemesofwork.view'),    
    path('<int:scheme_of_work_id>/edit', views.edit, name='schemesofwork.edit'),
    path('<int:scheme_of_work_id>/delete', views.delete, name='schemesofwork.delete_item'),
    path('<int:scheme_of_work_id>/publish', views.index, name='schemesofwork.publish_item'),
    path('<int:scheme_of_work_id>/save', views.save, name="schemesofwork.save"),
    path('', views.index, name='schemesofwork.index'), 
]