"""MRBS URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from app01 import views













from django.shortcuts import  HttpResponse

def yuan(request):

    return HttpResponse("Yuan")

def test01(request):

    return HttpResponse("test01")

def test02(request):

    return HttpResponse("test02")

def test03(request):

    return HttpResponse("test03")


def test04(request):

    return HttpResponse("test04")

def test05(request):

    return HttpResponse("test05")



def add(request):
    return HttpResponse("add")
def delete(request,id):
    return HttpResponse("delete")
def change(request,id):
    return HttpResponse("change")
def list_view(request):
    return HttpResponse("list_view")


def get_urls2():

    temp=[]
    temp.append(url(r"^add/",add))
    temp.append(url(r"^(\d+)/delete/",delete))
    temp.append(url(r"^(\d+)/change/",change))
    temp.append(url(r"^$",list_view))
    return temp

def get_urls():


    temp=[]
    print("_registry",admin.site._registry)

    for model,admin_class_obj in admin.site._registry.items():
         print("model",model) # 所有的注册模型表

         # < class 'app01.models.Book'>----->     "book"  "app01"
         # < class 'app01.models.Room'>----->     "room"  "app01"
         # print("===>",model._meta.model_name)
         # print("===>",model._meta.app_label)

         model_name=model._meta.model_name
         app_label=model._meta.app_label
         temp.append(url(r"%s/%s/"%(app_label,model_name),(get_urls2(),None,None)))


    return temp





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^book/', views.book),


    url(r"^yuan/",(get_urls(),None,None))


]
