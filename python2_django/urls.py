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
    #Chemin vers la page d'administration
    path("admin/", admin.site.urls),
    # Chemin pour les sessions d'enquêtes
    path('sessions/', views.session_list, name='session_list' ),
    path('sessions/create', views.session_create, name='session_create' ),
    path('sessions/delete/<int:id>/', views.session_delete, name="session_delete"),
    path('sessions/changestatus/<int:id>/', views.session_change_state, name="session_change_state"),
    path('sessions/edit/<int:id>/', views.session_edit, name="session_edit"),
    
    # Chemin vers les réponses à l'enquête
    path('sessions/<int:id>/summary', views.answer_summary, name="answer_summary"),
    #path('sessions/<int:id>/answer', views.answer_create, name="answer_create"),
    
    # Inclusion des pages d'authentification Django
    path("accounts/", include('django.contrib.auth.urls')),
    
    # Chemin vers l'acceuil
    path("", views.home_display, name = "home")
]
