"""
URL configuration for python2_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sessions/", views.session_list, name='session_list' ),
    path("sessions/create", views.session_create, name='session_create' ),
    path('sessions/delete/<int:id>/', views.session_delete, name="session_delete"),
    path('sessions/enable/<int:id>/', views.session_enable, name="session_enable"),
    path('sessions/disable/<int:id>/', views.session_disable, name="session_disable"),
    path('sessions/edit/<int:id>/', views.session_edit, name="session_edit"),
    path('sessions/<int:id>/summary', views.answer_summary, name="answer_summary"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("", views.home_display, name = "home")
]
