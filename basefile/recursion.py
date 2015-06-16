#coding:utf-8
#rec  function
#python 2.7.6

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print fact(100)

#后续需要继续优化

