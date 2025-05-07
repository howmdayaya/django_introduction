from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #配置users信息操作路由
    path('user/',views.indexUsers,name='indexusers'),
    path('user/add/',views.addUsers,name='addusers'),
    path('user/insert/',views.insertUsers,name='insertusers'),
    path('user/del/<int:uid>',views.delUsers,name='delusers'),
    path('user/edit/<int:uid>',views.editUsers,name='editusers'),
    path('user/update/',views.updateUsers,name='updateusers'),
]

