class MyClass:
    # 公共方法
    def getName(self):
        return self.name

    # 公共方法
    def setName(self, name):
        self.name= name
        # 在类的内部可以直接调用私有方法
        self.__outName()
    # 私有方法
    def __outName(self):
        print("Name = {}".format(self.name))

myClass = MyClass()
#导入inspece模块
import inspect

#获取MyClass类中的所有方法
methods = inspect.getmembers(myClass, predicate=inspect.ismethod)
print(methods)


#输入类方法的名称
for method in methods:
    print(method[0])

print("----------------")

#调用setName方法
myClass.setName("Bill")

print(myClass.getName())

myClass._MyClass__outName()

# 抛出异常，因为"__outName"方法在MyClass类中并不存在
print(myClass.__outName())


