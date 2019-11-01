from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test$', views.statis_test),  # 静态文件
    url(r'^index$', views.index),  # 静态文件
    url(r'^show_upload$', views.show_upload),  # 显示上传文件页面
    url(r'^upload_handle$', views.upload_handle),  # 上传文件处理
    url(r'show_area$', views.show_area),  # 分页

]
