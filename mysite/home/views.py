# -*- coding: utf-8 -*-
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from home.checkcode import gcheckcode

#@login_required
def index(request):
    return  render(request, 'home/index.html' , context=locals()) 
@login_required 
def index2(request):
    return  render(request, 'home/index2.html' , context=locals()) 
   
#登录  http://localhost:8000/sigin/
def sigin(request):   
    href = '/' 
    return  render(request, 'home/login.html' , context=locals()) 

#注册  http://localhost:8000/register/
def register(request):
    g_checkcode = gcheckcode(request)#验证码送前台验证
    href = '/' #注册成功，重新定向
    return  render(request, 'home/register.html' , context=locals()) 

