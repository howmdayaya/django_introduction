from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.urls import reverse

from myapp.models import Users
# Create your views here.
def home(request):
    # raise Http404("Error in home view")
    # print(reverse('home'))#通过name反向解析出url路径

    #使用model类

    # 添加数据
    # ob = Users() #实例化一个新的对象（空对象）
    # ob.name = "李四"
    # ob.age = 24
    # ob.phone = "12345678923"
    #  #新对象就是添加 已存在对象则是修改
    # ob.save()#保存到数据库中，id会自动生成

    #删除数据
    # mod = Users.objects #获取model类的对象
    # user = mod.get(id=4) #获取id为4的数据
    # print(user.name)
    # user.delete()#删除数据

    #修改数据
    # ob = Users.objects.get(id = 3)#获取id为3的数据
    # ob.name = "王武"#修改name字段的值为"王武"
    # ob.save()#保存到数据库中

    #查询数据
    # mod = Users.objects #获取model类的对象
    # ulist = mod.all() #获取所有数据
    # ulist = mod.filter(name="张三") #获取name为"张三"的数据，返回一个QuerySet对象，可迭代
    # ulist = mod.filter(age__gt=21) #获取age大于21的数据，返回一个QuerySet对象，可迭代
    # ulist = mod.filter(age__lt=21) #获取age小于21的数据，返回一个QuerySet对象，可迭代
    # ulist = mod.filter(age__gte=20) #获取age大于等于20的数据，返回一个QuerySet对象，可迭代
    # ulist = mod.order_by("age") #获取age升序的数据，返回一个QuerySet对象，可迭代
    # ulist = mod.order_by("age")[:2] #获取age升序的数据，返回一个QuerySet对象，可迭代，取前2条数据
    # ulist = mod.order_by("-age") #获取age降序的数据，返回一个QuerySet对象，可迭代

    # for u in ulist: #遍历所有数据
    #     print(u.id, u.name, u.age, u.phone, u.addtime)
    return HttpResponse("<h1>Hello, world. You're at the Home Page.</h1>")


#浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all()
        context = {"userslist":ulist} #将查询到的数据传递给模板
        return render(request,"myapp/users/index.html",context) #加载模板
    except:
        return HttpResponse("没有找到用户信息！")
#加载添加用户信息表单
def addUsers(request):
    pass
#执行用户信息添加
def insertUsers(request):
    pass
#执行用户信息删除
def delUsers(request,uid=0):
    pass
#加载修改用户信息表单
def editUsers(request,uid=0):
    pass
#执行用户信息修改
def updateUsers(request):
    pass