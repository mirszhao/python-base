#coding:utf-8
__author__ = 'Administrator'

class Animal(object):
    def run(self):
        print('Animal......')


class Dog(Animal):
    def run(self):
        print('Dog running......')

    def eat(self):
        print('Eating meat......')

class Cat(Animal):
    def run(self):
        print('Cat running......')


dog = Dog()

dog.run()
dog.eat()


cat = Cat()

cat.run()


a = list()

b = Animal()

c = Dog()

print isinstance(a,list)

print isinstance(b,Animal)

print isinstance(c,Dog)

print isinstance(c,Animal) # 子类也是父类的一个实例



#多态 ： 父类变量指向子类对象


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Cat())

# 获得对象信息

#type() 判断对象类型

print type(123)

print type(Animal())


#当使用if 进行判断类型时 使用types的内置常量

import types

print  types.StringType
print type('abc') ==types.StringType


#类型的本身 TypeType

print type(int) ==types.TypeType

#isinstance()

#isinstance()
#判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

#能用type() 判断的基本类型也可以用isinstance() 判断：


#由于str 和unicode 都是从basestring 继承下来的，所以，还可以把上面的代码简化为：

#-------------------------------------------------------

#dir() 获得一个对象的所有属性和方法   dir()函数

#print dir('ABC')

#print dir(Animal())

#仅仅把属性和方法列出来是不够的，配合getattr() 、setattr() 以及hasattr() ，我们可以直接操作一个对象的状态：

#hasattr(obj,'x') #有属性x吗

#setattr(obj, 'y', 19) # 设置一个属性'y'



#如果试图获取不存在的属性，会抛出AttributeError 的错误：


#getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404



#-------------------------面向对象高级编程------------------------------------

#__slots__

#动态给实例绑定属性和方法

class PageInfo(object):
    pass


#给实例绑定属性和方法

page = PageInfo()


page.pp = 2

print page.pp

def set_age(self,age):
    self.age = age

#动态给实例 添加方法
from types import MethodType

page.set_age = MethodType(set_age,page,PageInfo)

page.set_age(25)

print page.age

#也可以给类绑定方法

#Student.set_score = MethodType(set_score, None, Student)

#使用  使用__slots__


#想限制class的属性，比如只允许Student实例添加name 和age

#Python 允许在定义class 的时候，定义一个特殊的__slots__ 变量，来限制该class 能添加的属
#性：

class Catalog(object):
    __slots__ =('name','age') #用tuple定义允许绑定的属性名称


cc = Catalog()

cc.name = "ddd"
#cc.score="222"


#__slots__ 定义的属性仅对当前类起作用，对继承的子类是不起作用的：

#除非在子类中也定义__slots__ ，这样，子类允许定义的属性就是自身的__slots__ 加上父类的__slots__



#-----使用@property 把一个方法编程属性 调用的-------------------------------------------------------------

#通过get set方式获取属性未免有些太麻烦，有没有能检查参数 又能用类似属性这样简单
#的方式来访问类的变量。


#@property 的实现比较复杂，我们先考察如何使用。把一个getter 方法变成属性，只需要加上@property 就可以了，
#此时， @property 本身又创建了另一个装饰器@score.setter ，负责把一个setter 方法变成属性赋值，于是，我们就拥
#有一个可控的属性操作：

class Teacher(object):

    @property
    def score(self): #类似于get方法
        return self.__score

    @score.setter  #score是根据上面的@property来判定的

    def score(self,value):  #类似于set方法
        if not isinstance(value,int):
            raise ValueError('score must be an integer')

        if value< 0 or value > 100:
            raise ValueError('score must between 0~100')

        self.__score = value



ttt = Teacher()

ttt.score = 60

print ttt.score

# 也可以设置为只读属性

#------------------------------------------多重继承--------------------------

# 需要继承多个类的 类  中间使用逗号进行分割就可以

#通过多重继承   一个子类就可以同时获得多个父类的所有功能


#Mixin  主线都是单一继承 如果需要混入 额外的功能，通过多重继承就可以实现

#Mixin 的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin 的功
#能，而不是设计多层次的复杂的继承关系。


#由于Python 允许使用多重继承，因此，Mixin 就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用Mixin 的设计。


#---------------------------定制类-----------------------------------------

#__str__   类似于Java中的tostring



class Mirs(object):
    def __init__(self):
        pass

    def __str__(self):
        return 'Mirs Object toString()'


print Mirs()



# __repr__ = __str__


# __iter__  想被用于for in循环  该方法返回一个迭代对象

# for循环就会调用该迭代对象的next()方法，拿到循环的下一个值
#类里面需要提供 __iter__和 next方法

#这样就可以像 list那样可以进行 for in

#-----------------__getitem__----------------------

#可以获取到指定的数据项 该方法貌似实现了 类的数组功能

class Fib2(object):
    def __getitem__(self, n):

        a,b = 1,1
        for x in range(n):
            a,b = b, a+b

        return a




fib2 = Fib2()

print fib2[10]

#list 切片的方法
print range(100)[5:10]

# __getattr__








































