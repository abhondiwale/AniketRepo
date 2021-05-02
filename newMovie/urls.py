from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from newMovie import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('movinfo/<int:pk>', views.movies_review, name='movinfo'),
    path('search', views.search, name='search'),
    path('insert', views.insertmovie, name='insert')]
