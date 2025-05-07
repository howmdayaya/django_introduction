from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Hello, world. You're at the Home Page.</h1>"
        "<h3>Welcome to my-django-demo!</h3>"
        "<a href='/user'>用户管理系统</a><br>"
        "<a href='/playground'>django-官网演示案例</a>"
    )