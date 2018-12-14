class ClassA(object):

    num_A = 1

    def foo_A(self):
        pass

    def __str__(self):
        return 'this is ClassA'


class ClassB(ClassA):

    num_B = 2

    def __init__(self, name='ClassB'):
        super(ClassB, self).__init__()
        self.name = name

    def foo_B(self):
        pass

print(ClassA.__dict__)  # 类对象的__dict__不包含基类的属性
print('==========================')    
print(dir(ClassA))  # 会返回当前类以及它的所有基类的`__dict__`键值列表
print('==========================')
print(ClassB.__dict__)  # 类对象的__dict__不包含基类的属性    
print('==========================')
print(dir(ClassB))  # 会返回当前类以及它的所有基类的`__dict__`键值列表

objB = ClassB()
print('==========================')
print(objB.__dict__)
objB.grade = 123
print('==========================')
print(objB.__dict__)
print('==========================')
print(dir(objB))
lst = dir(objB) 
lst.remove('name')
lst.remove('grade')
print('==========================')
print(lst == dir(ClassB))   # dir(obj)除去obj绑定的属性和dir(class)得到内容的一样







