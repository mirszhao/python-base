#coding:utf-8
#high function  高阶函数
#python 2.7.6


#传入函数

#map/reduce

#map() 函数接收两个参数，一个是函数，一个是序列， map 将传入的函数依次作用到序列的每个元素，
#并把结果作为新的list 返回。

def f(x):
	return x*x

print map(f,[1,2,3,4,5])


#reduce reduce 把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce 把结果
#继续和序列的下一个元素做累积计算，其效果就是：

def add(x,y):
	return x+y


sum = reduce(add,map(f,[1,2,3,4,5]))

print sum

def fn(x,y):
	return x*10+y


def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7}

#排序 算法
#对于两个元素x 和y ，如果认为x < y ，则返回‐1 ，如果认为x == y ，则返回
#0 ，如果认为x > y ，则返回1 ，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。

print sorted([66,55,88,99])

#sorted也可以接收一个自定义排序函数

def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0

print sorted([66,55,88,99],reversed_cmp)


#忽略大小写的比较方法
def cmp_ignore_case(s1,s2):
    u1 = s1.upper();
    u2 = s2.upper();

    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0

#函数作为返回值

def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

#可以先不返回结果
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum



lazy = lazy_sum(1,2,3,5,8)

print lazy()


#匿名函数：lambda   lambda x：x*x  只可以有一个表达式。

print map(lambda x:x*x,[1,3,5])

#冒号前表示函数参数   只能有一个表达式，不用写return 返回值就是该表达式的结果
#也可以吧一个匿名函数赋值给变量  f = lambda x:x*x












