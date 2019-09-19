#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/19 下午3:37
# @IDE     : PyCharm
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
    # print("registry ->", wrapper.registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    """
    执行顺序：函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行
        execute decorator(<function f1 at 0x107403d90>)
        execute decorator(<function f2 at 0x1074038c8>)
        running main()
        registry -> [<function f1 at 0x107403d90>, <function f2 at 0x1074038c8>]
        running f1()
        running f2()
        running f3()
    """
    main()
