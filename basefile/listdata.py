 #coding:utf-8 
 #file  list
# python  2.7.6

classmates=['Sean','Mirs','Tracy']

print classmates

print len(classmates)

print classmates[0] #索引超出时 系统会报错

# len(classmates)-1

#获取最后一个元素  -1，类推  -2 。。

print classmates[-1]

#将数据插入到指定的位置，会把原位置的元素往后挤

classmates.insert(1,'Sean-insert')
print classmates
#删除末尾的元素

print 'pop-',classmates.pop()
print classmates

# pop(i)删除指定位置的元素。

#替换指定位置的元素
classmates[1] ="replaceElement"

#list也可以嵌套
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)