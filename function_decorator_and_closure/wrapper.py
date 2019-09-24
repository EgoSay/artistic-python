#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/19 下午4:40
# @IDE     : PyCharm
"""装饰器模块"""
import time
import functools
registry = list()


def test_order(func):
    """
    验证装饰器执行顺序
    :param func:
    :return: a wrapper function
    """
    print("execute decorator(%s)" % func)

    def wrapper():
        """大多装饰器会在内部自定义一个函数然后将其返回"""
        global registry
        registry.append(func.__name__)
        func()
        return registry
    return wrapper


def clock(func):
    """在每次调用被装饰的函数时计时，然后把经过的时间、传入的参数和调用的结果打印出来"""
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked






