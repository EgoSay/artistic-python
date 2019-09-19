#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/19 下午4:40
# @IDE     : PyCharm

registry = list()


def decorator(func):
    """
    作为例子这里装饰器返回的函数与通过参数传人的相同, 实际上，大多装饰器会在内部自定义一个函数然后将其返回
    :param func:
    :return:
    """
    print("execute decorator(%s)" % func)
    registry.append(func)
    return func
