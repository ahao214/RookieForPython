# 使用super函数

class Animal:
    def __init__(self):
        print("Animal init")

class Bird(Animal):
    # 为Bird类的构造方法增加一个参数(hungry)
    def __init__(self, hungry):
        # 调用Animal类的构造方法
        super().__init__()
        self.hungry = hungry
    def eat(self):
        if self.hungry:
            print("已经吃了虫子")
            self.hungry=False
        else:
            print("已经吃过饭了，不饿了")
b = Bird(False)
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self, hungry):
        # 调用Bird类的构造方法，如果为super函数指定参数，第一个参数需要是当前类的类型(SongBird)
        super(SongBird,self).__init__(hungry)
        self.sound = '向天再借五百年'

    def sing(self):
        print(self.sound)

sb = SongBird(True)
sb.sing()
sb.eat()
