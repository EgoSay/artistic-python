#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/19 下午3:37
# @IDE     : PyCharm
import function_decorator_and_closure.wrapper as wrapper
from function_decorator_and_closure.wrapper import test_order as decorator


@decorator
def f1():
    print("running f1().........")


@decorator
def f2():
    print("running f2().........")


def f3():
    print("running f3().........")


def main():
    print("running main()..........")
    print("registry ->", wrapper.registry)
    f1()
    f2()
    f3()
    print("registry ->", wrapper.registry)


if __name__ == '__main__':

    main()
    """输出结果:
        execute decorator(<function f1 at 0x1015271e0>)
        execute decorator(<function f2 at 0x10c370950>)
        running main()..........
        registry -> []
        running f1().........
        running f2().........
        running f3().........
        registry -> [<function f1 at 0x1015271e0>, <function f2 at 0x10c370950>]
    """
