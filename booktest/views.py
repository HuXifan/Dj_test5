from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


# 装饰器：实验禁止ip访问功能
# def blocked_ips(view_func):
#     def wrapper(request, *view_args, **view_kwargs):
#         # 获取浏览器段的ip地址
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')
#         else:
#             return view_func(request, *view_args, **view_kwargs)
#     return wrapper


def statis_test(request):
    '''静态文件'''
    print(settings.STATICFILES_FINDERS)
    # ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder')
    # 查找文件的顺序，Django本身查找过程:先去配置的目录下找，找不到再去应用下的static找
    return render(request, 'booktest/static_test.html')


# /index
def index(request):
    '''首页'''
    # 获取浏览器段的ip地址
    # user_ip = request.META['REMOTE_ADDR']
    print('index')
    # num = 'a' +1  # error
    return render(request, 'booktest/index.html')
