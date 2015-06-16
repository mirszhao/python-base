 #coding:utf-8 
# python  2.7.6
print 'Hello world!!!'

print '100+200= ' ,100+200

#100+200= 300
#name = raw_input()

#print name

#--------------------------------

#print 'Hello ,',name

#name2= raw_input("please input your name:")

a=-100
if a>=0:
	print a
else:
	print -a

print 'I \'am a learning \\python'


print r"i\' \\\am" #自然字符串



#多行数据
print '''line1
	line2
	line3
'''
print 3>2

print 10/3
print 10.0/3

print ord('A')

print chr(65)

print u"中文"

print u'中文'.encode('utf-8')
a=len(u'ABC')


print 'Hello,%s'% 'world'

#list

classmates=['Micheal','Bob','Tracy']
print classmates

print len(classmates)

for i in classmates:
	print i


#tuple

students=('AAA','BBB','CCC')

print students

tt=(1)#会默认为括号
print tt

tt1=(1,)
print tt1

# if 的使用
age=3;
if age >18:
	print 'default'
elif age>=6:
	print 'teenager'
else:
	print 'kid'


names=['Michael','Bob','Tracy']

for name in names:
	print name

for x in range(10):#从0开始 包含头不包含尾
	print x

n=10
while n>0:
	n=n-1
	print n


dicts = {'aaa':95,'bbb':75,'tracy':60}
print dicts['aaa']

dicts['aaa'] =66

print dicts['aaa']

print dicts

if 'ddd' in dicts:
	print dicts['ddd']
else:
	print 'none this dict'

print dicts.get('ddd')

#删除也是需要验证是否有
if 'ddd' in dicts:
	dicts.pop('ddd')

print set([1,2,3])

#ord() 和 chr() 函数   通过逗号连接

print 'A--ascii--',ord('A')

print '65 is char--',chr(65)


# u

print u"中文"
print u'中文'.encode('utf-8')

#格式化显示  和 C语言保持一致。  %s %d %f %x    %s永远起作用

print "Hello,%s" %'world'
print "Hello,%s,iam %d" %('world',32)
















