from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('signin',views.signin,name='signin'),
    path('contact',views.contact,name='contact'),


]