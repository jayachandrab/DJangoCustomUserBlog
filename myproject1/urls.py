"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import MorningGreetingView

urlpatterns = [
    path('api/blog/',include('blog.api.urls','blog_api')),
    path('api/account/',include('account.api.urls','acount_api')),
    path('admin/', admin.site.urls),
    path('blog/',include("blog.urls",'blog')),
   
    path('',include("ap1.urls")),
    #path('about/', TemplateView.as_view(template_name="about.html")),
    path('about/', MorningGreetingView.as_view()),



    # RestFramework
    
    #path('accounts/',include('django.contrib.auth.urls'))
   
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
