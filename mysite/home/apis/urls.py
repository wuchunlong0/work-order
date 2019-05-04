# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^registerapi/', views.registerapi, name="registerapi"),   
    url(r'^loginapi/', views.loginapi, name="loginapi"),            
]