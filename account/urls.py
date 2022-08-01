from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account', views.account, name='account'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
#    path('signin', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
]
