# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import checkcode
from . import views
urlpatterns = [    
    url(r'^index/', views.index, name="index"),
    url(r'^index2/', views.index2, name="index2"),
    
    url(r'^checkcodeGIF/', checkcode.checkcodeGIF, name="checkcodeGIF"),
    url(r'^getcheckcode/', checkcode.getcheckcode, name="getcheckcode"),
]