
from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # 获取最新的5个问题

    """ 
    output = ', '.join([q.question_text for q in latest_question_list])
    列表推导式  [expression for item in iterable if condition]  用于快速生成列表
    if condition 可选  用于过滤列表中的元素
    遍历最新问题列表 将问题文本拼接成字符串，以“，”分隔组成新列表返回给前端
        """
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {"latest_question_list": latest_question_list}
    return render(request,"playground/index.html", context)

def detail(request, question_id):
    """ try:
        question = Question.objects.get(pk=question_id) # pk 是主键的缩写  用于获取指定主键的对象
    except Question.DoesNotExist: # 如果没有找到指定主键的对象  抛出异常
        raise Http404("Question does not exist-就是没找到") # 抛出异常  返回404错误页面 """
    
    #简写  get_object_or_404() 需要导入
    # pk=question_id 这是一个查询条件，意味着要查找 Question 表中主键值等于 question_id 的记录。
    # 此处是关键词参数传递  不是赋值
    question = get_object_or_404(Question, pk=question_id) # 如果没有找到指定主键的对象  抛出异常  返回404错误页面
    return render(request, "playground/detail.html", {"question": question})

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")