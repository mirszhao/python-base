#coding:utf-8
#iteration  迭代
#python 2.7.6

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:  #打印结果并不是按写的顺序  默认迭代 key
	print key  


#迭代 value

for value in d.itervalues():
	print value

for k, v in d.iteritems():
	print k,',',v


for ch in 'ABC':
	print ch

#判断对象是否可迭代

from collections import Iterable

print isinstance('abc',Iterable)
#整数不可迭代

#list实现 java类似的下表循环 使用内置函数 enumrate

for i,value in enumerate(['A','B','C']):
	print i,value

#在python中同时迭代两个值是非常常见的

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x,y


#列表生成式：  内置 用来创建list 的生成式

print range(1,11)

#但是要生成[1x1,2x2,...]时怎么办1.循环L.append(ixi)   2.列表生成式


print [x*x for x in range(1,11)]

#写列表生成式时，把要生成的元素x * x 放到前面，后面跟for 循环

#for 循环后面还可以加上if 判断，这样我们就可以筛选出仅偶数的平方：

print [x*x for x in range(1,11) if x%2==0]


print [m+n for m in 'ABC' for n in 'XYZ'] #双重循环生成全排列

#列表生成式样也可以使用两个参数
d = {'x': 'A', 'y': 'B', 'z': 'C' }

print [k+'='+v for k,v in d.iteritems()]

#将集合内所有大写字母变小写
L = ['Hello', 'World', 'IBM', 'Apple']

print [s.lower() for s in L]


print isinstance(1,str)# 判断是否是字符串


#生成器——————————————一边循环 一边计算的机制 成为生成器———————————————————————————————————

#直接创建列表收到内存限制 列表容量肯定是有限的
#创建一个 generator   将列表生成式的[] 修改为()即可
g = (x*x for x in range(10))

print g

#创建L 和g 的区别仅在于最外层的[] 和() ， L 是一个list，而g 是一个generator

#打印generator 的next()

print g.next() #基本上不用
#正确的迭代方法
for n in g:
	print n


#generator 非常强大。如果推算的算法比较复杂，用类似列表生成式的for 
#循环无法实现的时候，还可以用函数来实现。










