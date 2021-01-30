from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="accounts.index"),
    path('register/', views.RegisterUserView.as_view(), name='accounts.register'),
    path('team-permissions/', include('app.teampermissions.urls')),
]
