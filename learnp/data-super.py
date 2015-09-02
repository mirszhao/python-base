__author__ = 'mirs'
#coding:utf-8

#高级特性

#--------------------------切片--------------------------------

def testSlice():
    L = ['Mirs','Jim','User','Liming']
    print L[0:3]# 从索引0开始取，直到索引为3，但不包括3 注意，3是索引 不是取得个数
    print L[:3] #如果从0开始，0可以省略
    print L[1:3]
    #倒数第一个元素的索引是-1
    print L[-2:]
    print L[-2:-1]

    L = range(100)

    #11-20个数
    print L[10:20]

    #前10个数，每两个取一个
    print L[:10:2]
    #所有数，每五个取一个
    print L[::5]

    #只写[:]就可以原样复制一个list

    #tuple 也可以使用切片操作
    print (0, 1, 2, 3, 4, 5)[:3]

    #字符串或Unicode字符串u'xxx'也可以看成一种list

    print 'ABCDEFG'[:3]
    print 'ABCDEFG'[::2]

#testSlice()


#---------------------------------迭代-----------------------------------------------

def testIter():
   dic = {'a': 1, 'b': 2, 'c': 3}
   for key in dic:
       print key


   for value in dic.itervalues():# dic.itervalues()
       print value

   for k1, v in dic.iteritems():
       print k1, ',', v

   for ch in 'ABCDFGR':
       print ch

#testIter()

#---------------------------------列表生成式-----------------------------------------------
#python内置的非常简单却强大的可以用来创建list的生成式。

def listCreator():
    L1 = range(1, 11)
    for x in L1:
        print x

    L2 = [x*x for x in L1]

    print L2

    L3 = [x*x for x in L1 if x%2 == 0]
    print L3

    #使用两层for循环 全排列
    print [m+n for m in 'ABC' for n in 'XYZ']
    import os
    #列出当前目录下所有文件和目录名
    print os.listdir('.')

    #列表生成式同样也可以使用两个变量来生成list
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print [k+'='+v for k, v in d.iteritems()]
#listCreator()

#---------------------------------生成器-----------------------------------------------
#通过列表生成式，我们可以创建一个列表，但是受到内存限制，列表容量肯定是有限的，而且
#过多的创建元素 却只访问前面几个元素，那么后面绝大多数的元素占用的空间都白白浪费了。

#边循环边计算的机制，称为生成器。

#创建一个generator 有很多种方法，第一种方法很简单，只要把一个列表生成式的[] 改成()
#就创建了一个generator

def testGenerator():
    g = (x*x for x in range(10))
    print g
    print g.next()
    #正常的做法是使用for循环，因为generator也是可迭代对象
    #我们创建一个generator 后，基本上永远不会调用next()方法
    for n in g:
        print n

#testGenerator()

#--------对于逻辑复杂的generator，类似列表生成式的for循环无法实现的时候  ，可以用函数来实现。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a+b
        n = n+1


fib(6)

#fib 是普通函数定义了运算规则，要把fib函数变成generator 只需要把print b 改为 yield b就可以了

def fibG(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

#如果函数中包含一个yield关键字，那么这个函数就不是一个普通函数，而是一个generator

print fibG(6)
#generator 和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回 再次执行从上次返回的yield
#语句处继续执行。











