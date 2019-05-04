"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from home import views

# from django.views.generic import TemplateView, ListView, View
# class IndexView(TemplateView):
#     template_name = 'home/index.html'
# url(r'^$', IndexView.as_view()),

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),

    url(r'^register/', views.register, name="register"),    
    url(r'^sigin/', views.sigin, name="sigin"),
        
    url(r'^home/', include('home.urls')),
    url(r'^apis/', include('home.apis.urls')), 
    
    url(r'^$', RedirectView.as_view(url='/home/index/')), 
    
    url(r'^ask/', include('ask.urls')),
]
