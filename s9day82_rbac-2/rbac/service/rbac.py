# by luffycity.com
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import  HttpResponse,redirect


def reg(request,current_path):
    # 校验权限1(permission_list)
    permission_list = request.session.get("permission_list", [])
    flag = False
    for permission in permission_list:

        permission = "^%s$" % permission

        ret = re.match(permission, current_path)
        if ret:
            flag = True
            break
    return flag

class ValidPermission(MiddlewareMixin):

    def process_request(self,request):


        # 当前访问路径
        current_path = request.path_info

        # 检查是否属于白名单
        valid_url_list=["/login/","/reg/","/admin/.*"]

        for valid_url in valid_url_list:
            ret=re.match(valid_url,current_path)
            if ret:
                return None


        # 校验是否登录

        user_id=request.session.get("user_id")

        if not user_id:
            return redirect("/login/")


        #校验权限1(permission_list)
        permission_list = request.session.get("permission_list",[])  # ['/users/', '/users/add', '/users/delete/(\\d+)', 'users/edit/(\\d+)']
        flag=reg(request,current_path)

        if not flag:
            return HttpResponse("没有访问权限！")

        return None

        # 校验权限2

        # permission_dict=request.session.get("permission_dict")
        #
        # for item in permission_dict.values():
        #       urls=item['urls']
        #       for reg in urls:
        #           reg="^%s$"%reg
        #           ret=re.match(reg,current_path)
        #           if ret:
        #               print("actions",item['actions'])
        #               request.actions=item['actions']
        #               return None
        #
        # return HttpResponse("没有访问权限！")
