class MyClass:
    def method1(self):
        print("method1")
    def default(self):
        print("method2")
my = MyClass()

#判断method1是否在my中存在
if hasattr(my, 'method1'):
    my.method1()
else:
    print("method1方法不存在")

# 判断method2是否在my中存在
if hasattr(my, 'method2'):
    my.method2()
else:
    print("method2方法不存在")


method = getattr(my, 'method2', my.default)
method()

def method2():
    print("动态添加的method2")

setattr(my, 'method2', method2)
my.method2()