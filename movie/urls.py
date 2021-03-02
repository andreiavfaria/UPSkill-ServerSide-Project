"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('search/', views.movie_search, name='movie_search'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/review/', views.movie_review, name='movie_review'),
    path('<int:movie_id>/review/edit', views.edit_review, name='movie_edit_review'),

]
