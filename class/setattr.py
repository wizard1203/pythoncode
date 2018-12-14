# -*- coding: utf-8 -*-
class Foo:
    x=1
    aaaaa = 12
    def __init__(self,y):
        self.y=y
        self.aaa = 1

    def __getattr__(self, item):
        if item not in self.__dict__.keys():
            print('----> from getattr:the attr doesn\'t exist')
            return None
        else:
            print('----> the attr exist')
        return self.__dict__[item]

    def prints(self):
        print('print something')

    #def __getattribute__(self, item):
    #    print('----> from __getattribute__')
    #    #super(Foo,self).__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('----> from setattr')
        # self.key=value #这就无限递归了,你好好想想
        # self.__dict__[key]=value #应该使用它

    def __delattr__(self, item):
        print('----> from delattr')
        # del self.item #无限递归了
        if item in self.__dict__.keys():
            self.__dict__.pop(item)

#__setattr__添加/修改属性会触发它的执行
f1=Foo(10)
print('===========')
print(f1.__dict__) # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
print('===========')
f1.z=3
print('===========')
print(f1.__dict__)

print('===========')
print(f1.aaa)
print('===========')
print(f1.x)
#__delattr__删除属性的时候会触发
print('===========')
f1.__dict__['a']=3#我们可以直接修改属性字典,来完成添加/修改属性的操作
print('===========')
del f1.a
print('===========')
del f1.bbb
print('===========')
print(f1.__dict__)
print('===========')
f1.xxxxxx
print('===========')
f1.prints()
print('===========')
#__getattr__只有在使用点调用属性且属性不存在的时候才会触发
