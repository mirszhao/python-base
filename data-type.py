__author__ = 'Administrator'
#coding:utf-8

def func1():
#1.print
    print 'Hello world!'
    #raw_input()  等待控制台输入

    #base
    a = 100
    if a >= 0:
        print(a)
    else:
        print -a


    #整数运算永远是精确的   永远是整数 只会舍
    #浮点数 运算应该是精确地

    print 10/3
    print 5/3
    print 5/3.0

    print 'i \'am "liming" '

    #boolean  True  False  布尔值可以用 and or not 运算


    #空值用None表示

    #变量
    a = 1;
    answer = True;

    #常量 Python中 通常用全部大写的变量表示常量

    PI = 3.14159265359
    #整数除法永远是整数，即使除不尽 要做精确地除法，只要把其中一个整数换成浮点数就可以

    #字符串和编码

    #python字符串 。Python 提供了ord()和chr()函数，可以把字母和对应的数字相互转换。

    print ord('A')

    print chr(65)

    print u'中文'
    print u'中文'.encode('utf-8')

    print len(u'中文')
    print len(u'中文'.encode('utf-8'))

    #格式化 %d %f %s %x
    print 'Hello,%s'%'world！'
    print 'Hi, %s, you have $%d.'%('Mirs',10000)
    #格式化整数和浮点数还可以指定是否补0 和整数与小数的位数
    print '%2d-%03d'%(3,1) #位数数字指定，补0需要加0
    print '%.2f'%3.1415126

#list  列表  有序集合  可以随时添加和删除其中的元素
def func_list():
    classmates = ['Michael','Bob','Tracy']

    print classmates
    print len(classmates)
    #按索引访问 从0开始 越界会报错 list index out of range
    print classmates[0]
    print classmates[-1]#从末尾取数据
    #从末尾删除 pop  classmates.pop()
    #删除 指定位置的元素 pop(i)  i是索引位置

    #替换可以 直接覆盖
    #list里面数据类型也可以不同，比如
    L = ['Apple', 123, True]

    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print len(s)
    print len(s[2])
    print s[2][1]



def func_tuple():
    #元组tuple 。tuple 和list 非常类似，但是tuple 一旦初始化就不能修改，
    ctuple = ('Mirs', 'Liming', 'Tom')
    ts = (1, 2)
    #定义一个空的tuple
    t = ()
    tt = (1,)

    #可变的tuple  tuple 的每个元素，指向永远不变,如果要创建一个内容也不变的list，必须保证tuple
    #的每个元素都不变。

    vart = ('a', 'b', ['A', 'B'])

    vart[2][0] = 'X'
    vart[2][1] = 'Y'

    print vart


def func_if_for_while():
    #条件判断

    age = 20

    if age >= 18:
        print 'your age is', age

    else:
        print 'your is is', age


    if age >= 18:
        print 'adult'

    elif age >= 6:
        print 'teenager'

    else:
        print 'kid'


    #if 判断条件还可以简写

    if age:
        print 'True'

    #只要x是非零数值、非空字符串、非空list 就判断为True

    #循环

    names =['mirs', 'liming', 'sean']

    for name in names:
        print name

    #所以for x in ... 循环就是把每个元素代入变量x ，然后执行缩进块的语句。

    #幸好Python 提供一个range()函数，可以生成一个整数序列，
    #比如range(5)生成的序列是从0 开始小于5 的整数：
    sum = 0
    for name in range(101):
        sum = sum + name

    print sum


    #while
    sum =0
    n = 99

    while n > 0:
        sum = sum + n
        n = n -2

    print sum


#在看 raw_input

#birth = raw_input('birth:')

# raw_input 永远以字符窜的形式返回  数字类型 可以用 int()方法进行转换


def func_dict():
    #dict
    #Python 内置了字典：dict 的支持，dict 全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具
    #有极快的查找速度。

    d = {'Mirs': 100, 'Liming': 75, 'Tracy': 85}

    print d['Mirs']

    #dict 就是第二种实现方式，给定一个名字，比如'Michael' ，dict 在内部就可以直接计算出Michael 对应的存放成绩的
    #“页码”，也就是95 这个数字存放的内存地址，直接取出来，所以速度非常快。

    d['Liming'] = 76 # 多次赋值会覆盖

    #如果值不存在  会报错

    #解决值不存在的问题有两种方式 1. 使用in 来判断  2 get方法  不存在时返回None 或自己制定value

    #d = {'Mirs': 100, 'Liming': 75, 'Tracy': 85}

    #print d['Hehe'] 会报错

    print 'Hehe' in d
    print d.get('Hehe')
    print d.get('Hehe',-1)

    #print d.pop('Hehe')删除不存在的key也会报错
    print d.pop('Mirs') #删除并返回删除的value值



#set
def func_set():
    #set 和dict 类似 也是一组key的集合，但不存储value 由于key不重复，在set中 没有重复的key

    #要创建一个set 需要提供一个list作为输入集合：  重复元素会自动被过滤

    s = set([1, 2, 3, 4, 5])
    print s

    #add(key) 添加元素到set中 可以重复添加 但是没有效果

    s.add(8)
    print s

    #remove(key)可以删除元素

    #set 可以看成数学意义上的无序和无重复元素的集合，因此，两个set 可以做数学意义上的交集、并集等操作
    s1 = set([1,2,3])
    s2 = set([2,3,4])

    print s1 & s2
    print s1 | s2
    #set 和dict 的唯一区别仅在于没有存储对应的value，但是，set 的原理和dict 一样，所以，同样不可以放入可变对象，


#list   sort
#str replace(pre, new )


#函数
#数据类型转换  int() float str   unicode bool

#定义函数

def my_abs(x):

    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


#print my_abs(-100)
#如果没有return 语句，函数执行完毕后也会返回结果，只是结果为None

#空函数
def nop():
    pass

#参数类型检查

#返回多个值   Python 函数返回的仍然是单一值
#Python 的函数返回多值其实就是返回一个tuple，但写起来更方便。

#函数的参数 默认参数

def power(x, n=2):
    s = 1
    while  n>0:
        n = n-1
        s = s*x

    return s


print power(5)
print power(5, 3)

#默认参数不要使用可变对象  这样在多次调用时，如果未指定 将会出现不正确的情况,指针指定的对象地址是固定的


#可变参数
#传入的参数个数可变

def calc(*numbers):
    sum = 0
    for n in numbers: #for in 会自动校验是否为空
        sum = sum + n*n

    return sum


#print calc()
#定义可变参数和定义list 或tuple 参数相比，仅仅在参数前面加了一个* 号。在函数内部，参数numbers 接收到的是一
#个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0 个参数：

#如果已经存在一个list 或者 tuple








