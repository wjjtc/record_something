"""
增强函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
"""

#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：

# @log
# def now():
#     print('2024-6-1')


# 把@log放到now()函数的定义处，相当于执行了语句：

# now = log(now)
# 现在的now函数已经变成了log返回的wrapper函数了。
'''
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
这个3层嵌套的decorator用法如下：

@log('execute')
def now():
    print('2024-6-1')
执行结果如下：

>>> now()
execute now():
2024-6-1
和两层嵌套的decorator相比，3层嵌套的效果是这样的：

>>> now = log('execute')(now)
我们来剖析上面的语句，首先执行log('execute')，
返回的是decorator函数，本质上是@decorator。再调用返回的函数，
参数是now函数，返回值最终是wrapper函数。
'''

"""
由于函数也是对象 有name属性 now函数变成了wrapper函数，name属性也会变。
可以使用wrapper.__name__ = func.__name__把wrapper函数的name改成func的name，
但更好的方法是使用functools.wraps的decorator，把原函数的属性复制到wrapper函数中：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

"""


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time
import functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, (end - start) * 1000))
        return result
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z



f = fast(11, 22)
s = slow(11, 22, 33)
