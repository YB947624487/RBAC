

from stark.service.stark import site,ModelStark

from django.urls import reverse
from .models import *


from django.utils.safestring import mark_safe

class UserConfig(ModelStark):

    def edit(self,obj):

        #return mark_safe("<a href='%s/change'>编辑</a>"%obj.pk)
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url=reverse("%s_%s_change"%(app_label,model_name),args=(obj.pk,))
        print("_url",_url)



        return mark_safe("<a href='%s'>编辑</a>"%_url)

    def deletes(self, obj):
        # return mark_safe("<a href='%s/change'>编辑</a>"%obj.pk)
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        _url = reverse("%s_%s_delete" % (app_label, model_name), args=(obj.pk,))
        print("_url", _url)

        return mark_safe("<a href='%s'>删除</a>" % _url)

    def checkbox(self, obj):


        return mark_safe('<input type="checkbox">')

    list_display=[checkbox,"pk","name","age",edit,deletes]

site.register(UserInfo,UserConfig)




class BookConfig(ModelStark):
    list_display = ["pk","title"]

site.register(Book)


print("_registry ",site._registry)





