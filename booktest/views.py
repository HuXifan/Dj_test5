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


# /show_upload
def show_upload(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    '''处理上传文件'''
    # 1 获取上传的文件的处理对象
    pic = request.FILES['pic']
    print(type(pic))

    # 2 创建一个文件

    # 3 获取上传文件的内容,并写入创建的文件中

    # 4 在数据库中保存上传文件的记录

    # 5 返回
    return HttpResponse('ok')