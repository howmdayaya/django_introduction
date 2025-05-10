from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mytpdemo/index.html')

def demo1(request):
    """演示模板语法"""
    context = {}
    context['name'] = 'zhangsan'
    context['a'] = [10,20,30]
    context['hobby'] = ['编程','阅读','音乐']
    context['d'] = {'name':'张三','age':20,'gender':'男'}
    data = [
        {'name':'张三','age':20,'gender':1,'hobby':['编程','阅读','音乐'],'state':0},
        {'name':'李四','age':21,'gender':0,'hobby':['编程','阅读','音乐'],'state':1},
        {'name':'王五','age':22,'gender':1,'hobby':['编程','阅读','音乐'],'state':2},
        {'name':'赵六','age':23,'gender':0,'hobby':['编程','阅读','音乐'],'state':1},
        {'name':'钱七','age':24,'gender':1,'hobby':['编程','阅读','音乐'],'state':2},
    ]
    context['data'] = data
    context['time'] = datetime.now()
    context['title'] = '模板语法演示'
    context['content'] = '这是模板语法演示'
    context['m1'] = 100
    context['m2'] = 20
    return render(request,'mytpdemo/demo1.html',context)

def demo2(request):
    return render(request,'mytpdemo/demo2.html')

