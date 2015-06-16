#coding:utf-8
__author__ = 'Administrator'

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score


    def print_score(self):
        print('%s %s'%(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'






bart = Student('Sean ',33)

mirs = Student('mirs ',90)

bart.print_score()
print bart.get_grade()
mirs.print_score()
mirs.score =30 #此时可以任意修改
print mirs.get_grade()



#在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定
#义一个特殊的__init__ 方法，在创建实例的时候，就把name ， score 等属性绑上去：

#访问限制   属性前 双 下划线

class User(object):
    def __init__(self,name):
        self.__name = name

    def print_name(self):
        print "name is %s" %self.__name

    def get_name(self):
        return self.__name


user = User("Tom")

user.print_name()
#print user.__name 不可以访问
print user.get_name() #通过get和 set方法 可以对参数做检查

# 其实是可以访问的

print user._User__name #但是强烈不建议你这样做

#总的来说就是，Python 本身没有任何机制阻止你干坏事，一切全靠自觉。

#继承和多态



















































































































