#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/11 6:31 下午
# @IDE     : PyCharm


def fib():
    """利用迭代器写斐波那契数列"""
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = prev + curr, curr


f = fib()
for i in range(10):
    print(next(f))

