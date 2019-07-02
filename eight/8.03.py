#类代码块
class MyClass:
    #class 块中的语句，会立刻执行
    print("MyClass")
    count = 0
    def counter(self):
        self.count += 1

my = MyClass()
my.counter()
print(my.count)

my.counter()
print(my.count)

my.count="abc"
print(my.count)

my.name = "hello"
print(my.name)
