from django.shortcuts import render
from django.conf import settings


# Create your views here.
def statis_test(request):
    '''静态文件'''
    print(settings.STATICFILES_FINDERS)
    # ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder')
    # 查找文件的顺序，Django本身查找过程:先去配置的目录下找，找不到再去应用下的static找
    return render(request, 'booktest/static_test.html')
