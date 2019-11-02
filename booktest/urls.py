from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test$', views.statis_test),  # 静态文件
    url(r'^index$', views.index),  # 静态文件
    url(r'^show_upload$', views.show_upload),  # 显示上传文件页面
    url(r'^upload_handle$', views.upload_handle),  # 上传文件处理
    url(r'^show_area(?P<p>\d*)$', views.show_area),  # 分页
    url(r'^areas$', views.areas),  # 省市县选择页面
    url(r'^prov$', views.prov),  # 获取所有省级地区信息
    url(r'^city(\d+)$', views.city),  # 获取所有市级地区信息
    url(r'^dis(\d+)$', views.city),  # 获取所有县级地区信息

]
