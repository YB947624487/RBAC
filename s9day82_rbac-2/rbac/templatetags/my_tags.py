# by luffycity.com



from django import template

register=template.Library()

from rbac.service.rbac import reg

@register.simple_tag
def valid(link,request):
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(link,"html.parser")
    print(soup.a.get('href'))
    path=soup.a.get('href')

    flag=reg(request,path)

    if flag:
        return link
    else:return ""
