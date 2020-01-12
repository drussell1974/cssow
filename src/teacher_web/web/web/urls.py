"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from app.default import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # api lessons
    path('api/schemesofwork/<int:scheme_of_work_id>/lessons/', include('api.lessons.urls')),
    # api schemesofwork
    path('api/schemesofwork/', include('api.schemesofwork.urls')),
    # api default
    path('api/', include('api.default.urls')),
    # app lesson
    path('schemesofwork/<int:scheme_of_work_id>/lessons/', include('app.lesson.urls')),
    # app schemeofwork
    path('schemesofwork/', include('app.schemesofwork.urls')),
    # TODO: move to reference app
    path('reference/<int:reference_id>/edit', views.index, name="reference.edit"),
    # app default
    path('', include('app.default.urls')),    
]
