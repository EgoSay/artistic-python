#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/19 下午4:40
# @IDE     : PyCharm
"""装饰器模块"""
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


# def test_order2(func):
#     """
#     验证装饰器执行顺序
#     :param func:
#     :return: a wrapper function
#     """
#     print("execute decorator(%s)" % func)
#     registry.append(func)
#     return func




