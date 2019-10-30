from django.http import HttpResponse


class BlockIpMiddleware(object):
    '''中间件类'''
    EXCLUDE_IPS = ['10.10.21.29']  # 禁止列表

    # process_view 名字是Django预留的  位置参数， 和关键字参数
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        # 在视图函数调用之前会调用
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIpMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
            # 直接返回一个应答后，后续的视图就不在调用了，实现一种干预，
        else:
            return view_func(request, *view_args, **view_kwargs)


class TestMiddleware(object):
    '''中间件类'''

    def __init__(self):
        # 服务器重启之后接受第一个请求时调用
        print('__init__   ___')

    def process_request(self, request):
        # 产生request对象之后，url匹配之前调用
        print('process_request   ___')
        return HttpResponse('process_request')

    def process_view(self, request, view_func, *view_args, **view_kargs):
        # url匹配之后，视图调用之前调用;  view_func:接下来要被调用的视图函数的名字
        print('process_view ')

    def process_response(self, request, response):
        # 视图函数调用之后，内容返回给浏览器之前 调用。
        print('process_response')
        return response  # 返回值


'''
在类中定义中间件预留函数。
中间件函数都可以敢于整个应答过程，之前的装饰器改成中间件就是这样的原理，在process_view实现干预
__init__:服务器响应第一个请求的时候调用。
process_request:是在产生request对象，进行url匹配之前调用。
process_view：是url匹配之后，调用视图函数之前。   
process_response：视图函数调用之后，内容返回给浏览器之前。   
process_exception:视图函数出现异常，会调用这个函数。
'''


class ExceptionTest1Middleware(object):
    def process_exception(self, request, exception):
        # exception：异常对象
        # 视图函数发生异常时调用
        print('process_exception_______1___')
        print(exception + '___1____')

'''
Quit the server with CONTROL-C.
index
process_exception________2_____
process_exception_______1___
'''
'''注册多个中间件，顺序从下网上调 '''


class ExceptionTest2Middleware(object):
    def process_exception(self, request, exception):
        # exception：异常对象
        # 视图函数发生异常时调用
        print('process_exception________2_____')
        print(exception+'_2_____')
