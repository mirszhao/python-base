#coding:utf-8
#function
#python 2.7.6

'''
	abs()

	cmp(x,y)

	int('123')
	float('12.23')
	str(1.23)

	bool(1)
	unicode(100)


'''
#自定义绝对值函数
def my_abs(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')

	if x>0:
		return x
	else:
		return -x


print my_abs(-19999)

#print my_abs('A')

#pass  定义空函数   一般用作占位符，使程序能正常运行

def nop():
	pass



#return multiValue

import math

def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)

	return nx,ny

x,y = move(100,100,60,math.pi/6)

print x,'\n',y

#其实python返回的仍然是单一值，返回了一个tuple，写起来更加方便

c=move(100,100,60,math.pi/6)

print c


#默认参数

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x

	return s

#为了保证power(x)的正常运行

#def power(2)求平方的值  

def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x

	return s

#默认参数规则： 必须参数在前，默认参数在后2.变化大的参数放前面 变化小的放后面
#好处 降低调用函数的难度

#坑   函数在初始化的时候就被计算出来了  L指向对象[]  每次调用函数都记住了L的内容

# 所以  默认函数必须指向不变的对象



def add_end(L=[]):
	L.append('End')

	return L

print add_end()

print add_end()


#更正版

def add_Bate(L=None):
	if L is None:
		L=[]
	L.append('End')

	return L

print add_Bate()

print add_Bate()


#可变参数  传入的参数个数是可变的  *   其实在函数内部 接收到的是tuple，


def calc(*numbers):
	sum=0
	for n in numbers:
		sum =sum +n
	return sum



print calc(1)

#python 允许你在list或者tuple 前面加 *  把list或者tuple元素变成可变参数传进去。

nums=[1,2,3,4]

print calc(*nums)



#关键字参数 
'''
可变参数允许你传入0 个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
关键字参数允许你传入0个或者任意个含参数的名的参数，这些关键字参数在函数内图自动
 #组装一个dict



'''

def person(name,age,**kw):
	print 'name:',name,'age:',age,' ,other:',kw


print person('hehe',26)

print person('hehe',26,city='beijing')


kw ={'DDD':222,'FFF':555}

print person('eee','ffff',**kw) #简单的形式 该dict 转换为 关键字参数传递进去



#参数组合：使用顺序： 必选参数，默认参数，可选参数 和 关键字参数

'''
*args 是可变参数，args 接收的是一个tuple；
**kw 是关键字参数，kw 接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入： func(1, 2, 3) ，又可以先组装list 或tuple，再通过*args 传入： func(*(1, 2, 3)) ；
关键字参数既可以直接传入： func(a=1, b=2) ，又可以先组装dict，再通过**kw 传入： func(**{'a': 1, 'b': 2}) 。
使用*args 和**kw 是Python 的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''


def func(a,b,c=0,*args,**kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2)

func(1,2,3)  #print func(1,2,c=3)

func(1,2,3,'a','b')

func(1, 2, 3, 'a', 'b', x=99)






































