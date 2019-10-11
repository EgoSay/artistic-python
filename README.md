# The Programming art in python 🐍

## Introduction📖
> There are many beautiful usage in python, such as:
> - [The Function-Programming](#python中的函数): 函数式编程
> - [Object-Oriented Programming](#面向对象编程): 面向对象编程
> - [迭代器和生成器](#迭代器和生成器): 迭代器和生成器
> - [Concurrent Processing](): 并发处理
> - [Metaprogramming](): 元编程
> - [Regular expression](#正则表达式): 正则表达式
> - [The Design Patterns](): 设计模式
> - [Data Analysis](#数据分析): 数据分析

## python中的函数
#### 在 Python 中，函数是一等对象。

- 编程语言理论家把“一等对象”定义为满足下述条件的程序实体：

    ```
    1. 在运行时创建
    
    2. 能赋值给变量或数据结构中的元素
    
    3. 能作为参数传给函数
    
    4. 能作为函数的返回结果
    ```
- [高阶函数](first_class_function/higher_order_function.ipynb)
    >函数式语言通常会提供 map、 filter 和 reduce 三个高阶函数（有时使用不同的名称）。在
Python 3 中， map 和 filter 还是内置函数，但是可以用列表推导和生成器表达式替换

- [可调用类型](first_class_function/callable_type_examples.ipynb)

- [参数处理](first_class_function/parameter_processing.ipynb)
    >Python 最好的特性之一是提供了极为灵活的参数处理机制
    
#### [函数装饰器与闭包](function_decorator_and_closure/function_decorator_and_closure.md)
>装饰器本质上是python函数，它可以使其他函数在不需要做代码变动的情况下增加新的功能，装饰器返回值也是一个函数对象<p>
>类比[装饰器模式](https://www.runoob.com/design-pattern/decorator-pattern.html)
## 面向对象编程
- #### [对象引用](object_oriented_programming/docs/object_reference.md)
- #### [序列的修改、散列和切片](object_oriented_programming/vector_example)

## [迭代器和生成器](iterators_and_generators)
因为生成器完全实现了迭代器接口, 在 `Python` 中，大多数时候都把迭代器和生成器视作同一概念
>在 Python 语言内部，迭代器用于支持：
>1. for 循环
>2. 构建和扩展集合类型
>3. 逐行遍历文本文件
>4. 列表推导、字典推导和集合推导
>5. 元组拆包
>6. 调用函数时，使用 * 拆包实参

参考链接:
>[如何更好地理解Python迭代器和生成器](https://www.zhihu.com/question/20829330)
## 正则表达式
- [learn-regex](https://github.com/ziishaned/learn-regex)

## 数据分析
[Python数据分析实践](https://github.com/EgoSay/Data-Analysis)