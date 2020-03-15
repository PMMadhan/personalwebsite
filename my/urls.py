#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name = 'Home'),
    path('Portfolio', views.Portfolio, name = 'Portfolio'),
    path('Contact', views.Contact, name= 'Contact'),
]