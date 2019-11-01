from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from booktest.models import PicTest


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
    print(settings.FILE_UPLOAD_HANDLERS)
    # ('django.core.files.uploadhandler.MemoryFileUploadHandler',
    # 'django.core.files.uploadhandler.TemporaryFileUploadHandler')
    
    # num = 'a' +1  # error
    return render(request, 'booktest/index.html')


# /show_upload
def show_upload(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    '''处理上传文件'''
    # 1 获取上传的文件的处理对象,上床文件的处理对象可以获取到名字和内容
    pic = request.FILES['pic']  # request对象属性FILES,返回上传文件的处理对象
    # print(type(pic))
    # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>  # 上传文件大小不大于2.5M,文件放在内存中InMemory
    # <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>  # 文件大于2.5M文件放到一个临时文件Temporary中
    # print(pic.name)  # 可以获取上传文件的名字
    # pic.chunks()  # 分块的返回文件内容,是一个生成器,可以遍历它读取内容

    # 2 创建一个文件.拼接路径
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)  # 保存文件路径
    # 创建文件  二进制wb
    with open(save_path, 'wb') as f:
        # 3 获取上传文件的内容,并不断写入创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4 在数据库中保存上传文件的记录
    PicTest.objects.create(good_pic='booktest/%s' % pic.name)

    # 5 返回
    return HttpResponse('ok')
