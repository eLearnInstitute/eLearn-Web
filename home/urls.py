from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('others', views.others, name='others'),
    path('faculties', views.faculties, name='faculties'),
    
]
