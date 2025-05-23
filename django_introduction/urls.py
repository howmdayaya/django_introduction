"""
URL configuration for django_introduction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    #username:admin,password:123456
    path('admin/', admin.site.urls),

    path('',views.home,name='home'),
    #在当前总路由中添加子路由
    path('user/',include('myapp.urls')),
    path('playground/', include('playground.urls')),
    path('myweb/', include('myweb.urls')),
    path('mytpdemo/', include('mytpdemo.urls')),
]
