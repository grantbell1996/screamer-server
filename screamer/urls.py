"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from screamer_api.views.list_view import ListView
from django.conf.urls import include
from django.contrib import admin
from django.db import router
from rest_framework import routers
from django.urls import path
from screamer_api.views import register_user, login_user
from screamer_api.views import ActorView, MovieView, GenreView
from screamer_api.views.director_view import DirectorView
from screamer_api.views.review_view import ReviewView
from screamer_api.views.user_view import UserView


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'actors', ActorView, 'actor')
router.register(r'directors', DirectorView, 'actor')
router.register(r'movies', MovieView, 'movie')
router.register(r'genres', GenreView, 'genre')
router.register(r'reviews', ReviewView, 'review')
router.register(r'lists', ListView, 'list')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
]   
