# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from ask import views

urlpatterns = [
    url(r'^ask/', views.ask, name="ask"),   
    url(r'^list/(?P<page>\d*)?$', views.list, name="list"),    


]