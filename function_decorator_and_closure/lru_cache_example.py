#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/23 下午5:29
# @IDE     : PyCharm
import functools
import time

from function_decorator_and_closure.wrapper import clock


@clock
def fibonacci(n):
    """这种方法最简单， 但开销很大"""
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci_2(n):
    """利用lru_cache()优化"""
    if n < 2:
        return n
    else:
        return fibonacci_2(n - 2) + fibonacci_2(n - 1)


@functools.lru_cache()
@clock
def fibonacci_3(n):
    """利用生成器优化"""

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fibonacci(6))
    print(fibonacci_2(6))
    print(fibonacci_3(6))

