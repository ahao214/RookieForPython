# 静态方法和类方法
class MyClass:
    # 定义一个静态变量，可以被静态方法和类方法访问
    name = 'Bill'
    def __init__(self):
        print("MyClass的构造方法被调用")
        # 定义实例变量，静态方法和类方法不能访问该变量
        self.value = 20

    # 定义静态方法
    @staticmethod
    def run():
        # 访问MyClass类中的静态变量name
        print('*', MyClass.name, '*')
        print('MyClass的静态方法润被调用')

    # 定义类方法
    @classmethod
    def do(self):
        print(self)
        print('[',self.name, ']')
        print('调用静态方法run')
        self.run()

        print('成员方法do被调用')

    def do1(self):
        print(self.value)
        print('<', self.name, '>')
        print(self)

MyClass.run()

c = MyClass()
c.do()
print("MyClass2.name", '=', MyClass.name)
MyClass.do()
c.do1()
