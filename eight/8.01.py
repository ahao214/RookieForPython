# 创建一个Person类
class Person:
    # 定义setName方法
    def setName(self, name):
        self.name = name

    # 定义getName方法
    def getName(self):
        return self.name

    # 定义greet方法
    def greet(self):
        print("hello, I'm {name}.".format(name = self.name))


# 创建person1对象
person1 = Person()

# 创建person2对象
person2 = Person()

# 调用person1对象的setName方法
person1.setName("Bill Gates")

# 调用person2对象的name属性
person2.name = "Clinet"

# 调用person1对象的getName方法
print(person1.getName())

# 调用person1对象的greet方法
person1.greet()



# 调用person2对象的属性
print(person2.name)

# 调用person2对象的greet方法（另外一种调用方法的方式）
Person.greet(person2)
