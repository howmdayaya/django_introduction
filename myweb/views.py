from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'myweb/index.html')

# 简单视图
def res01(request):
    return HttpResponse('<h2>这是一个简单的视图</h2>')

# 错误视图
def res02(request):
    # return HttpResponseNotFound('<h2>Page not found</h2>')
    return Http404('<h2>Page not found</h2>') # 返回404错误页面

# 重定向视图
def res03(request):
    # return redirect('https://www.baidu.com') # 重定向到百度
    return redirect(reverse('home')) # 重定向到项目首页
    # context = {
    #     'title': '重定向视图',
    #     'content': '这是一个重定向视图',
    # }
    # return render(request, 'myweb/res03.html', context)

# 基于类的基本视图
# 视图类必须继承自View类，并重写get()方法，该方法用于处理GET请求
class MyView(View):

    def get(self, request):
        return HttpResponse('<h2>这是一个基于类的基本视图</h2>')
    
# josn数据的响应
def res05(request):
    data = [
        {'name': '张三','age': 18,'gender': '男',},
        {'name': '李四','age': 19,'gender': '女',},
        {'name': '王五','age': 20,'gender': '男',},
        {'name': '赵六','age': 21,'gender': '女',},
    ]
    return JsonResponse({'data':data}) # 返回json数据 默认接收字典数据

# Cookie的使用
def res06(respuest):
    # 访问Cookie
    name = respuest.COOKIES.get('name') # 获取Cookie

    # 获取当前的响应对象，用于设置Cookie
    response = HttpResponse(f'<h2>Cookie的使用-{name}</h2>')

    # 使用响应对象进行Cookie的设置
    response.set_cookie('name', 'zhangsan') # 设置Cookie


    # 返回响应对象，包含Cookie信息
    return response

# 测试request对象
def res07(request):
    # 获取请求方法
    method = request.method # 获取请求方法
    # 获取请求路径
    path = request.path # 获取请求路径
    # 获取请求参数
    params = request.GET # 获取请求参数
    # 获取请求头部信息
    headers = request.headers # 获取请求头部信息

    context = {
        'method': method,
        'path': path,
        'params': params,
        'headers': headers,
    }
    return HttpResponse(f'<h2>测试request对象-{context}</h2>')
