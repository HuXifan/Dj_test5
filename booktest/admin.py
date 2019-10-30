from django.contrib import admin
from booktest.models import AreaInfo


# 块的嵌入方式
class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    extra = 2  # 多余空行


# 表格嵌入方式
class AreaTabularInline(admin.TabularInline):
    # 写多类的名字
    model = AreaInfo
    extra = 2  # 多余空行


# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型管理类'''
    list_per_page = 10  # 指定每页显示十条
    # list_display 可写 模型类属性和模型类方法
    list_display = ['id', 'atitle', 'title', 'parent']
    actions_on_bottom = False  # 下拉列表框
    list_filter = ['aParent']  # 列表页右侧过滤栏
    search_fields = ['atitle']  # 列表页上的搜索框
    # fields = ['aParent', 'atitle']  # 显示字段顺序
    fieldsets = (
        ('基本', {'fields': ['atitle']}),  # 元祖 必须加,  逗号
        ('高级', {'fields': ['aParent']}),  # 元祖 必须加,  逗号
    )

    # inlines = [AreaStackedInline]  # 块的嵌入方式
    inlines = [AreaTabularInline]  # 块的嵌入方式


admin.site.register(AreaInfo, AreaInfoAdmin)  # 注册
