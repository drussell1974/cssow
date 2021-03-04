from django.urls import path, include

from . import views

urlpatterns = [
    path("profile/", views.index, name="accounts.index"),
    path('register/', views.RegisterTeacherView.as_view(), name='accounts.register'),
    path('team-permissions/', include('app.teampermissions.urls')),
    path("", views.index, name="accounts.index"),
]
