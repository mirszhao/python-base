#coding:utf-8
#tuple file 元组
#python 2.7.6

classmates=('Sean','Jack','Mirs')

print classmates
print classmates[0]

t=(1,2)
print t

t=()

print t

t=(1,) #元组只有一个元素时

print t

#可变的元组,  指向永远不变，但指向本身的list是可变的

t=('a','b',['A','B'])

print t

t[2][0]='C'

print t











