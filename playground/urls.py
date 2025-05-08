from django.urls import path
from . import views

#添加命名空间  防止命名冲突  防止url反向解析时出现错误
app_name = 'playground'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]