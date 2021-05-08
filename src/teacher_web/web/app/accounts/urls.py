from django.urls import path, include

from . import views

urlpatterns = [
    path("profile/", views.index, name="accounts.index"),
    path("delete/", views.delete, name="accounts.delete"),
    path('register/', views.RegisterTeacherView.as_view(), name='accounts.register'),
    path('join/', views.JoinAsTeacherView.as_view(), name='accounts.join'),
    path('team-permissions/', include('app.teampermissions.urls')),
    path("", views.index, name="accounts.index"),
]
