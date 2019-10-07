from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from app01 import models
from functools import wraps


# def check_login(f):
#     @wraps(f)
#     def inner(request, *args, **kwargs):
#         if request.session.get("is_login") == "1":
#             return f(request, *args, **kwargs)
#         else:
#             return redirect("/login/")
#     return inner
#
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = models.User.objects.filter(username=username, password=password)  # [User Obj, ]
#         if user:
#             # 登陆成功
#             request.session["is_login"] = "1"
#             # request.session["username"] = username
#             request.session["user_id"] = user[0].id
#             # 1. 生成特殊的字符串
#             # 2. 特殊字符串当成key,在数据库的session表中对应一个session value
#             # 3. 在响应中向浏览器写了一个Cookie Cookie的值就是 特殊的字符串
#
#             return redirect("/index/")
#
#     return render(request, "login.html")
#
#
# @check_login
# def index(request):
#     user_id = request.session.get("user_id")
#     # 根据id去数据库中查找用户
#     user_obj = models.User.objects.filter(id=user_id)
#     if user_obj:
#         return render(request, "index.html", {"user": user_obj[0]})
#     else:
#         return render(request, "index.html", {"user": "匿名用户"})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 如何判断用户名和密码对不对
        user = auth.authenticate(username=username, password=pwd)
        if user:
            ret = user.is_authenticated()
            print(ret)
            print("-" * 120)

            # 将登录的用户封装到request.user
            auth.login(request, user)
            return redirect("/index/")
    return render(request, "login.html")


@login_required
def index(request):
    print(request.user.username)
    print("=" * 120)
    ret = request.user.is_authenticated()
    print(ret)
    return render(request, "index.html")




def logout(request):
    auth.logout(request)
    return redirect("/login/")


# def register(request):
#     from django.contrib.auth.models import User
#
#     # User.objects.create(username="alex", password="alexdsb")  # 不用这个
#     # User.objects.create_superuser()
#     user_obj = User.objects.create_user(username="alex5", password="alexdsb")
#     # 校验密码是否正确
#     ret = user_obj.check_password("alex1234")
#     print(ret)
#     # 修改密码
#     user_obj.set_password("alex3714")
#     user_obj.save()
#     return HttpResponse("o98k")


def register(request):

    # User.objects.create(username="alex", password="alexdsb")  # 不用这个
    # User.objects.create_superuser()
    user_obj = models.UserInfo.objects.create_user(username="alex5", password="alexdsb")
    # 校验密码是否正确
    ret = user_obj.check_password("alex1234")
    print(ret)
    # 修改密码
    user_obj.set_password("alex3714")
    user_obj.save()
    return HttpResponse("o98k")
