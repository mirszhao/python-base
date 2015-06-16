#coding:utf-8
#decorate 装饰器
#python 2.7.6
import functools
def now():
    print '2014-1-1'


f = now

f() #函数也是一个对象，函数对象可以赋值给变量，通过变量也能调用该函数。

#函数对象有一个__name__ 属性，可以拿到函数的名字:双下划线
print now.__name__
print f.__name__

#本质上，decorator 就是一个返回函数的高阶函数。
def log(func):
    @functools.wraps(func) #将原始函数属性复制到wrapper中
    def wrapper(*args,**kw):
        print "call %s()"%func.__name__
        return func(*args, **kw)

    return wrapper

#使用Python 的@语法 在每个函数上使用

@log
def test1():
    print "Hello python..."

test1()

# equals test1 = log(test1)

#wrapper() 函数的参数定义是(*args, **kw) ，因此， wrapper() 函数可以接受任意参数的调用。在wrapper() 函数内，
#首先打印日志，再紧接着调用原始函数。


#如果decorator 本身需要传入参数，那就需要编写一个返回decorator的高阶函数

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'%(text, func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator


@log2("text----")
def now2():
    print '2014-11-8'

now2()
print now2.__name__

#原理解析  now = log2('execute')(now)

#我们来剖析上面的语句，首先执行log2('execute') ，返回的是decorator 函数，再调用返回的函数，参数是now 函
#数，返回值最终是wrapper 函数。
#但是返回的函数 已经变成了 wrapper
#------------------------------------------------------

















































































































































