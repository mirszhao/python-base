#coding:utf-8
#advanced
#python 2.7.6

L=['AA','FF','EE','RR','WW']

#获取前三个
r=[]

n=3
for i in range(n):
	r.append(L[i])

print r

#切片操作 Slice  通过 : 实现 L[0:3] 表示，从索引0 开始取，直到索引3 
#为止，但不包括索引3。即索引0，1，2，正好是3 个元素。
print L
print 'L[0:3]--',L[0:3] # 取索引为 0,1,2

print 'L[:3]--',L[:3]

print 'L[1:3]--',L[1:3]

print 'L[-1]--',L[-1]

print 'L[-2:]--',L[-2:]

print 'L[-2:-1]--',L[-2:-1]

'''
后10 个数：
>>> L[‐10:]

前11-20 个数：
>>> L[10:20]

前10 个数，每两个取一个：
>>> L[:10:2]

所有数，每5 个取一个：
>>> L[::5]

只写[:] 就可以原样复制一个list：


>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)

字符串 或者 Unicode字符串  也可以看成一种list

>>> 'ABCDEFG'[:3]
'ABC'

>>> 'ABCDEFG'[::2]
'ACEG'

'''



