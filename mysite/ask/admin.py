# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . models import Ask, Answer
 
@admin.register(Ask)
class AskAdmin(admin.ModelAdmin):    
    list_display = ('id','name','title','uploadimg','edit','status','date')
 
 
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):    
    list_display = ('id','name','title','uploadimg','edit','date')