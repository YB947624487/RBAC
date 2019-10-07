from django.shortcuts import render,HttpResponse

# Create your views here.



from rbac.models import *


def users(request):
    user_list=User.objects.all()

    return render(request,"users.html",locals())


import re
def add_user(request):


    return HttpResponse("add user.....")

def roles(request):

    role_list=Role.objects.all()

    return render(request,"roles.html",locals())
from rbac.service.perssions import *

def login(request):

    if  request.method=="POST":

        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        user=User.objects.filter(name=user,pwd=pwd).first()
        if user:
            ############################### 在session中注册用户ID######################
            request.session["user_id"]=user.pk

            ###############################在session注册权限列表##############################



            # 查询当前登录用户的所有角色
            # ret=user.roles.all()
            # print(ret)# <QuerySet [<Role: 保洁>, <Role: 销售>]>

            # 查询当前登录用户的所有权限
            initial_session(user,request)


            return HttpResponse("登录成功！")


    return render(request,"login.html")

