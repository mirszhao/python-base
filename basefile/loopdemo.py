#coding:utf-8
#for  while :
#python 2.7.6

names =['Sean','Mirs','Index']

for name in names:
	print name

sum=0
for x in range(101): # 0,100
	sum = sum+x

print sum

# while 
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print sum

#raw_input()读取的内容永远以字符串的形式返回，如果为int需要使用int('str')

