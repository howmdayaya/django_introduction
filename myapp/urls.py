from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),

    #配置users信息操作路由
    path('',views.indexUsers,name='indexusers'),
    path('add/',views.addUsers,name='addusers'),
    path('insert/',views.insertUsers,name='insertusers'),
    path('del/<int:uid>',views.delUsers,name='delusers'),
    path('edit/<int:uid>',views.editUsers,name='editusers'),
    path('update/',views.updateUsers,name='updateusers'),
    
]

