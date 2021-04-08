from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="default"),
    path('accounts/', include('app.accounts.urls')),
    path('academic-year', views.academic_year, name="default.academic-year")
]