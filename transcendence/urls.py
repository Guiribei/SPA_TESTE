# your_app/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
	path('logout', views.logout, name='logout'),
]
