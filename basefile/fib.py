#coding:utf-8
#fid 斐波拉契数列
#python 2.7.6

def fid(max):
	n,a,b=0,0,1
	while n<max:
		print b

		a,b=b,a+b
		n=n+1

print fid(6)

#将函数变为generator  将 print改为 yield即可 


#这就是定义generator 的另一种方法。如果一个函数定义中包含yield 关键字，那么这个函数就不再是一个普通函数，
#而是一个generator：
def fid2(max):
	n,a,b=0,0,1
	while n<max:
		yield b

		a,b=b,a+b
		n=n+1

print fid2(6)


