from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='department.index'),
    path('all', views.viewall, name='department.all'),
    path('new', views.edit, name='department.new'),
    path('delete_unpublished', views.delete_unpublished, name="department.delete_unpublished"),
    path('<int:department_id>/schemesofwork/', include('app.schemesofwork.urls')),
    path('<int:department_id>', views.index, name='department.view'),    
    path('<int:department_id>/edit', views.edit, name='department.edit'),
    path('<int:department_id>/pathways/', include('app.ks123pathways.urls')),
    path('<int:department_id>/topics/', include('app.topic.urls'))
    #path('<int:department_id>/publish', views.publish, name='department.publish_item'),
]