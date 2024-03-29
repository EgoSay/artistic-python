#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/11 12:11 下午
# @IDE     : PyCharm
from array import array
import math


class Vector2d:

    """typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用"""
    typecode = 'd'

    def __init__(self, x, y):
        """在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，以防调用 Vector2d 函数时传入不当参数"""
        self.__x = float(x)
        self.__y = float(y)

    """@property 装饰器把读值方法标记为特性"""
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        """定义 __iter__ 方法，把 Vector2d 实例变成可迭代的对象，这样才能拆包（例如， x, y = my_vector）"""
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """__repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串；
        因为Vector2d 实例是可迭代的对象，所以 *self 会把 x 和 y 分量提供给 format 函数"""
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        """把 typecode 转换成字节序列"""
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        """使用 __hash__ 方法把 Vector2d 实例变成可散列的"""
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
            components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
