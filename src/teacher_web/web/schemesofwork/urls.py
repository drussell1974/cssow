from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schemesofwork'),    
    path('new', views.index, name='schemesofwork.new'),
    path('edit/<int:id>', views.index, name='schemesofwork.edit'),
    path('delete/<int:id>', views.index, name='schemesofwork.delete_item'),
    path('edit/<int:id>', views.index, name='schemesofwork.publish_item'),
]