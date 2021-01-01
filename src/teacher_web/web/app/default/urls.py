from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="default"),
    path('accounts/profile/', views.profile, name="profile")
]