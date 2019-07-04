# 重写普通方法和构造方法
class A:
    def __init__(self):
        print("A类的构造方法")

    def method(self):
        print("A类的method方法")

class B(A):
    def __init__(self):
        print("B类的构造方法")
    def method(self):
        print("B类的method方法")

a = A()
a.method()

b = B()
b.method()

print("----------------------")


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("已经吃了虫子")
            self.hungry = False
        else:
            print("已经吃过饭了，不饿了")

b = Bird()
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        self.sound="向天再借五百年"
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
