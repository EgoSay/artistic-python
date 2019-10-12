#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/11 6:31 下午
# @IDE     : PyCharm
import numpy as np


def fib():
    """利用迭代器写斐波那契数列"""
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = prev + curr, curr


def cal(array):
    """验证生成器只能遍历一次"""
    for item in array:
        yield item


if __name__ == '__main__':

    print("""========== example1, 斐波那契数列==========""")
    f = fib()
    for i in range(10):
        print(next(f))

    print("""======== example2, 验证生成器只能遍历一次==========""")
    arr = np.random.randint(100, size=8)
    print("生成随机数组为:{0}".format(arr))
    result = cal(arr)
    print("下面是 sum 求和会遍历一次生成器👇")
    all_sum = sum(result)
    print(all_sum)
    print("第二次遍历生成器， 没有任何输出打印")
    for r in result:
        print(r / all_sum)
