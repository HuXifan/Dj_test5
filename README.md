# Dj_test5

## 静态文件
项目中的CSS、图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。在html页面中调用时，也需要指定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。
静态文件可以放在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。

### 示例

1）在test5/settings.py文件中定义静态文件存放的物理目录。

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
2）在项目根目录下创建static目录，再创建img、css、js目录。

3）在booktest/views.py中定义视图static_test。

def static_test(request):
    return render(request,'booktest/static_test.html')
4）在booktest/urls.py中配置url。

    url(r'^static_test/$',views.static_test),
5）在templates/booktest/下创建static_test.html文件。

<html>
<head>
    <title>静态文件</title>
</head>
<body>
<img src="/static/img/sg.png"/>
</body>
</html>
6）保存图片到static/img/目录下，名称为sg.png。

7）运行服务器.
### 配置静态文件
Django提供了一种配置，可以在html页面中可以隐藏真实路径。
1）在test5/settings.py文件中修改STATIC_URL项。

# STATIC_URL = '/static/'
STATIC_URL = '/abc/'
2）刷新浏览器，图片找不到了

3）修改templates/booktest/static_test.html如下：

<html>
<head>
    <title>静态文件</title>
</head>
<body>
修改前：<img src="/static/img/sg.png"/>
<hr>
修改后：<img src="/abc/img/sg.png"/>
</body>
</html>
3）刷新浏览器，

4）查看网页源代码，发现可以网址和真实地址之间没有关系。

为了安全可以通过配置项隐藏真实图片路径，在模板中写成固定路径，后期维护太麻烦，可以使用static标签，根据配置项生成静态文件路径。

1）修改templates/booktest/static_test.html如下：

<html>
<head>
    <title>静态文件</title>
</head>
<body>
修改前：<img src="/static/img/sg.png"/>
<hr>
修改后：<img src="/abc/img/sg.png"/>
<hr>
动态配置：
{%load static from staticfiles%}
<img src="{%static "img/sg.png" %}"/>
</body>
</html>

说明：这种方案可以隐藏真实的静态文件路径，但是结合Nginx布署时，会将所有的静态文件都交给Nginx处理，而不用转到Django部分，所以这项配置就无效了。

## 中间件
Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性，其它的MVC框架也有这个功能，名称为IoC。
Django在中间件中预置了五个方法，这五个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

1）初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件。
def __init__(self):
    pass
    
2）处理请求前：在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象.
def process_request(self, request):
    pass
    
3）处理视图前：在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。
def process_view(self, request, view_func, *view_args, **view_kwargs):
    pass
    
4）处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。
def process_response(self, request, response):
    pass
    
5）异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。
def process_exception(self, request,exception):
    pass


## admin站点
1）准备工作：创建管理员的用户名和密码。
2）使用：在应用的admin.py中注册模型类
### 控制管理页展示
类ModelAdmin可以控制模型在Admin界面中的展示方式，主要包括在列表页的展示方式、添加修改页的展示方式。
1）在booktest/admin.py中，注册模型类前定义管理类AreaAdmin。
管理类有两种使用方式：
注册参数
装饰器
注册参数：打开booktest/admin.py文件，注册模型类代码如下：
admin.site.register(AreaInfo,AreaAdmin)

## 列表页选项
### 页大小
每页中显示多少条数据，默认为每页显示100条数据，属性如下：

list_per_page=100
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10

### 操作选项的位置
顶部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。
actions_on_top=True
底部显示的属性，设置为True在底部显示，设置为False不在底部显示，默认为False。
actions_on_bottom=False
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    actions_on_top = True
    actions_on_bottom = True

### 列表中的列
属性如下：
list_display=[模型字段1,模型字段2,...]
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    list_display = ['id','atitle']

将方法作为列
列可以是模型字段，还可以是模型方法，要求方法有返回值。

1）打开booktest/models.py文件，修改AreaInfo类如下：
class AreaInfo(models.Model):
    ...
    def title(self):
        return self.atitle
        
2）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    list_display = ['id','atitle','title']

方法列是不能排序的，如果需要排序需要为方法指定排序依据。

admin_order_field=模型类字段


###  列标题
列标题默认为属性或方法的名称，可以通过属性设置。需要先将模型字段封装成方法，再对方法使用这个属性，模型字段不能直接使用这个属性。
short_description='列标题'
1）打开booktest/models.py文件，修改AreaInfo类如下：
class AreaInfo(models.Model):
    ...
    title.short_description='区域名称'
    
### 关联对象
无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员。

1）打开booktest/models.py文件，修改AreaInfo类如下：
class AreaInfo(models.Model):
    ...
    def parent(self):
        if self.aParent is None:
          return ''
        return self.aParent.atitle
    parent.short_description='父级区域名称'
2）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    list_display = ['id','atitle','title','parent']
    
### 又侧过滤栏
属性如下，只能接收字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。

list_filter=[]
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    list_filter=['atitle']
    
### 搜索框
属性如下，用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。

search_fields=[]
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    search_fields=['atitle']

### 中文标题
1）打开booktest/models.py文件，修改模型类，为属性指定verbose_name参数，即第一个参数。
class AreaInfo(models.Model):
    atitle=models.CharField('标题',max_length=30)#名称
    ...
    
## 编辑页选项
### 显示字段顺序
属性如下：
fields=[]

2）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    fields=['aParent','atitle']
    
在下拉列表中输出的是对象的名称，可以在模型类中定义str方法用于对象转换字符串。

1）打开booktest/models.py文件，修改AreaInfo类，添加str方法。
class AreaInfo(models.Model):
    ...
    def __str__(self):
        return self.atitle

### 分组显示
属性如下：

fieldset=(
    ('组1标题',{'fields':('字段1','字段2')}),
    ('组2标题',{'fields':('字段3','字段4')}),
)
1）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    # fields=['aParent','atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
#### 说明：fields与fieldsets两者选一使用。

### 关联对象
在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种。
类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑。子类TabularInline：以表格的形式嵌入。
子类StackedInline：以块的形式嵌入。

1）打开booktest/admin.py文件，创建AreaStackedInline类。
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo#关联子对象
    extra = 2#额外编辑2个子对象
2）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    inlines = [AreaStackedInline]
    
用表格的形式嵌入。

1）打开booktest/admin.py文件，创建AreaTabularInline类。
class AreaTabularInline(admin.TabularInline):
    model = AreaInfo#关联子对象
    extra = 2#额外编辑2个子对象
2）打开booktest/admin.py文件，修改AreaAdmin类如下：
class AreaAdmin(admin.ModelAdmin):
    ...
    inlines = [AreaTabularInline]
    
## 重写模板
1）在templates/目录下创建admin目录

2）打开当前虚拟环境中Django的目录，再向下找到admin的模板，目录如下：
.../lib/python3.7.3/site-packages/django/contrib/admin/templates/admin
3）将需要更改文件拷贝到第一步建好的目录里，此处以base_site.html为例。
编辑base_site.html文件：

4）在浏览器中转到列表页面，其它后台的模板可以按照相同的方式进行修改。