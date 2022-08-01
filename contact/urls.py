from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
#    path('student', views.student, name='student'),
#    path('parent', views.parent, name='parent'),
#    path('mentor', views.mentor, name='mentor'),
    
]
