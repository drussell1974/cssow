from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="accounts.index"),
    path('register/', views.RegisterUserView.as_view(), name='accounts.register'),
    path('my-team-permissions/', views.my_team_permissions, name='accounts.my-team-permissions'),
]
