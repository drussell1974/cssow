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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from app.default import views

urlpatterns = [

    
    ### api ##
    
    # api resource
    path('api/schemesofwork/<int:scheme_of_work_id>/lessons/<int:lesson_id>/resources/', include('api.resources.urls')),
    # api lessons
    path('api/schemesofwork/<int:scheme_of_work_id>/lessons/', include('api.lessons.urls')),
    # api schemesofwork
    path('api/schemesofwork/', include('api.schemesofwork.urls')),
    # api default
    path('api/', include('api.default.urls')),
    
    ### app ###

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # app event-log
    path('schemesofwork/<int:scheme_of_work_id>/event-log/', include('app.eventlogs.urls')),
    # app content
    path('schemesofwork/<int:scheme_of_work_id>/curriculum-content/', include('app.content.urls')),
    # app lesson
    path('schemesofwork/<int:scheme_of_work_id>/lessons/', include('app.lessons.urls')),
    # app schemeofwork
    path('schemesofwork/', include('app.schemesofwork.urls')),
    # TODO: move to reference app
    path('reference/<int:reference_id>/edit', views.index, name="reference.edit"),
    # app default
    path('', include('app.default.urls')),    
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns