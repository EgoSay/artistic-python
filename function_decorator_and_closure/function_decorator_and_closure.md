### 装饰器基础知识
>装饰器是可调用的对象，其参数是另一个函数(被装饰的函数)，装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象<p>
#### Python何时执行装饰器
>函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行<p>
[示例代码](decorator_execute_order.py)<p>
>这里我联想到了 Java中的父类子类静态函数的执行顺序<p>
>```markdown
>    1. 父类中静态成员变量和静态代码块
>
>    2. 子类中静态成员变量和静态代码块
>    
>    3. 父类中普通成员变量和代码块，父类的构造函数
>    
>    4. 子类中普通成员变量和代码块，子类的构造函数
>```  

#### 利用装饰器还可以实现 "策略模式"
> 参考：[python实现策略模式](https://www.jianshu.com/p/e535d23dab0e) <p>
> [示例代码](strategy_mode_with_decorator.py)  
   
### 变量作用域与规则
>Python不要求声明变量， 但是在函数定义体中赋值的变量会识别为局部变量<p>
>[Demo](variable_scope_demo.py)

### 闭包
>闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量<p>
我的理解：[示例](closure_learning.ipynb)
>1. 首先它本质是一个函数<p>
>2. 这个函数引用了其他地方的变量， 这个变量在它函数内部没有定义且不是全局变量<p>
>3. 这个函数是不是匿名的没有关系， 关键是它能访问它本身这个函数定义体之外定义的非全局变量

>参考链接: <p>
>1. [深入浅出python闭包](https://zhuanlan.zhihu.com/p/22229197)
>2. [python中的闭包](https://www.the5fire.com/closure-in-python.html)

### 标准库中的装饰器
>`functools.lru_cache`: 它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算, 用于优化<p>
>[示例代码：优化斐波纳切数列的计算过程](lru_cache_example.py)

>`functools.singledispatch`:使用 `@singledispatch` 装饰的普通函数会变成泛函数 `generic function` : 根据第一个参数的类型，以不同方式执行相同操作的一组函
数<p>
>[示例代码](singledispatch_example.py)


### Github上发现一个大神关于装饰器的仓库: [wrapt](https://github.com/GrahamDumpleton/wrapt)



