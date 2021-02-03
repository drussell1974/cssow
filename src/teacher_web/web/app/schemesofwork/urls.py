from django.urls import include, path

from . import views

urlpatterns = [
    path('new', views.edit, name='schemesofwork.new'),
    path('delete_unpublished', views.delete_unpublished, name="schemesofwork.delete_unpublished"),
    path('<int:scheme_of_work_id>', views.index, name='schemesofwork.view'),    
    path('<int:scheme_of_work_id>/edit', views.edit, name='schemesofwork.edit'),
    path('<int:scheme_of_work_id>/publish', views.index, name='schemesofwork.publish_item'),
    #path('<int:scheme_of_work_id>/delete', views.index, name='schemesofwork.delete'),
    path('<int:scheme_of_work_id>/keywords/', include('app.keywords.urls')),
    path('', views.index, name='schemesofwork.index'), 
]