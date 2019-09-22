#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/22 21:44
# @IDE     : PyCharm

b = 8


def func1(a):
    """
    能正确打印， 因为b定义为全集变量
    :param a:
    :return:
    """
    print(a)
    print(b)


def func2(a):
    """
    执行函数func2会报错， 因为在函数中给b赋值了，python编译时判断其为局部变量
    :param a:
    :return:
    """
    print(a)
    print(b)
    b = 6



if __name__ == '__main__':
    func1(3)
    func2(1)

