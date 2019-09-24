#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/24 下午12:00
# @IDE     : PyCharm
from functools import singledispatch
from collections import abc
import numbers
import html

# 使用 @singledispatch 扩展一个生成 HTMl 的工具, 显示不同类型的 Python 对象:
#     - 默认情况下，在 <pre></pre> 中显示 HTML 转义后的对象字符串表示形式
#     - 为 str 对象显示的也是 HTML 转义后的字符串表示形式，不过放在 <p></p> 中，而且使用 <br> 表示换行
#     - int 显示为十进制和十六进制两种形式，放在 <pre></pre> 中
#     - 各个列表项目根据各自的类型格式化，整个列表则渲染成 HTML 列表


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{0}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(num):
    return '<pre>{0}:(0x{0:x})</pre>'.format(num)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    # print("=========>{0}".format(inner))

    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    # print(htmlize("hello"))
    # print(htmlize(42))
    print(htmlize([(3, 7), (1, 5)]))
    # print(htmlize(['alpha', 66, [(3, 7), (1, 5)]]))
