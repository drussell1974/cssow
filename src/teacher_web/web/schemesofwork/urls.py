from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schemesofwork'),  
    path('new', views.index, name='schemesofwork.new'),
    path('<int:scheme_of_work_id>', views.index, name='schemeofwork.view'),    
    path('<int:scheme_of_work_id>/edit', views.index, name='schemesofwork.edit'),
    path('<int:scheme_of_work_id>/delete', views.index, name='schemesofwork.delete_item'),
    path('<int:scheme_of_work_id>/publish', views.index, name='schemesofwork.publish_item'),
]