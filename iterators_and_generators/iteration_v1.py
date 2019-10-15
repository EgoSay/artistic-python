#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/12 12:09 下午
# @IDE     : PyCharm
import re
import reprlib


class Example1:
    """定义一个示例类, 通过索引从文本中提取单词, 它是一个可迭代对象"""

    def __init__(self, text):
        self.text = text
        # 匹配提取所有数字字母字符,  re 模块用法见: https://github.com/python/cpython/blob/3.7/Lib/re.py
        self.words = re.compile('\w+').findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        """reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式"""
        return '(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    e1 = Example1("hello world, i use 'python'、'Java', it's beautiful ")
    print(e1)
    print("-------------测试这个类示例可以迭代-----------")
    for word in e1:
        print(word)

    """因为同时也是序列, 可以按索引打印输出"""
    print("e1[1] = %s" % e1[1])
