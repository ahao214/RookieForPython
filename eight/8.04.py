#类的继承


# 父类
class ParentClass:
    def method1(self):
        print("method1")

#子类
class ChildClass(ParentClass):
    def method2(self):
        print("method2")

child = ChildClass()
child.method1()
child.method2()