from django.urls import path
from . import views
#导入类视图
from .views import MyView

app_name = 'myweb' #命名空间
urlpatterns = [
    path('', views.index, name='index'), #首页
    path('res01/', views.res01, name='res01'), #简单视图
    path('res02/', views.res02, name='res02'), #错误视图
    path('res03/', views.res03, name='res03'), #重定向视图
    path('res04/', MyView.as_view(), name='res04'), #基于类的基本视图
    path('res05/', views.res05, name='res05'), #响应json数据格式
    path('res06/', views.res06, name='res06'), # Cookie的使用
    path('res07/', views.res07, name='res07'), # 测试request对象
]