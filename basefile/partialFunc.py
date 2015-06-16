#coding:utf-8
#filename:patialFunc.py
#version:2.7.6
#按指定的进制进行转换 ，默认按十进制

print int('2334')

print int('2334',base=8)

print int('2334',16)

#可以设置一个默认值，这样不用每次都传递进制信息

def int2(x,base=2):  #转换二进制字符串
    return int(x,base)


print int2('100000')

#functools.partial

import functools
import mycompany.abc

int3 = functools.partial(int,base=2)

print int3('111111000000')
import sys
print sys.path
#sys.path.append('D:\\pythonsrc')
#sys.path.remove("D:\\pythonsrc")
print sys.path


#所以，简单总结functools.partial 的作用就是，把一个函数的某参数（不管有没有默认值）给固定住（也就是设
#置默认值），返回一个新的函数，调用这个新函数会更简单。

#最后创建偏函数时，要从右到左固定参数
#当函数的参数个数太多，需要简化时，使用functools.partial 可以创建一个新的函数，这个新函数可以固定住原函
#数的部分参数，从而在调用时更简单。

#导入的模块一定要在 python path下 这样才有效 否则找不到

mycompany.abc.test()



#别名
'''

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

'''

#可以优先使用 try块里的库

#作用域
#类似_xxx 和__xxx 这样的函数或变量就是非公开的（private），不应该被直接引用

mycompany.abc._private_1() #可以引用，但是并不是建议这样做

#安装第三方插件





























































































