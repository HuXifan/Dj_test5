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
        else:
            return view_func(request, *view_args, **view_kwargs)
