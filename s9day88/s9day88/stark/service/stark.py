# by luffycity.com
from django.conf.urls import url

from django.shortcuts import HttpResponse,render

class ModelStark(object):
    list_display=[]

    def __init__(self,model,site):
        self.model=model
        self.site=site
    def add(self, request):

        return HttpResponse("add")

    def delete(self, request, id):
        return HttpResponse("delete")

    def change(self, request, id):
        return HttpResponse("change")

    def list_view(self, request):
        print(self.model)
        print("list_dispaly",self.list_display)

        data_list=self.model.objects.all() # 【obj1,obj2,....】

        new_data_list=[]
        for obj in data_list:
            temp=[]
            for filed in  self.list_display:# ["pk","name","age",edit]

                if callable(filed):
                    val=filed(self,obj)
                else:
                    val=getattr(obj,filed)

                temp.append(val)

            new_data_list.append(temp)

        '''
        [
            [1,"alex",12],
           
                 ]

        '''

        print(new_data_list)

        return render(request, "list_view.html", locals())




    def get_urls_2(self):

        temp = []

        model_name=self.model._meta.model_name
        app_label=self.model._meta.app_label

        temp.append(url(r"^add/", self.add,name="%s_%s_add"%(app_label,model_name)))
        temp.append(url(r"^(\d+)/delete/", self.delete,name="%s_%s_delete"%(app_label,model_name)))
        temp.append(url(r"^(\d+)/change/", self.change,name="%s_%s_change"%(app_label,model_name)))
        temp.append(url(r"^$", self.list_view,name="%s_%s_list"%(app_label,model_name)))

        return temp

    @property
    def urls_2(self):
        return self.get_urls_2(), None, None


class StarkSite(object):
    def __init__(self):
        self._registry={}

    def register(self,model,stark_class=None):
        if not stark_class:
            stark_class=ModelStark

        self._registry[model] = stark_class(model, self)


    def get_urls(self):
        temp=[]
        for model,stark_class_obj in self._registry.items():
            model_name=model._meta.model_name
            app_label=model._meta.app_label
            # 分发增删改查
            temp.append(url(r"^%s/%s/"%(app_label,model_name),stark_class_obj.urls_2))

            '''
            url(r"^app01/userinfo/",UserConfig(Userinfo).urls_2),
            url(r"^app01/book/",ModelStark(Book).urls_2), 
            
            '''
        return temp

    @property
    def urls(self):

       return self.get_urls(),None,None

site=StarkSite()












