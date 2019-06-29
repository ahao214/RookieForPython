# object & class
class Person:
    __name = ''
    __email = ''

    # 构造函数
    def __init__(self,name,email):
        self.__name= name
        self.__email= email

    #方法 methods
    def setName(self,name):
        self.__name = name;
    def getName(self):
         return self.__name;

    def setEmail(self,email):
        self.__email = email;
    def getEmail(self):
        return self.__email;

    def toString(self):
        return  '{} is good looking,他的email是{}'.format(self.__name,self.__email)

# 实例化对象
# henry = Person()

# henry.setName("henry")
# henry.setEmail("hacoehcn@126.com")
# print(henry.getName())
# print(henry.getEmail())

bucky = Person("bucky","buck@126.com")
print(bucky.getEmail())
print(bucky.getName())

print(bucky.toString())

# 继承

class Customer(Person):
    __balance = 0

    def __init__(self,name,email,balance):
        self.__name= name
        self.__email = email
        self.__balance= balance
        super(Customer, self).__init__(name,email)
john = Customer("john","john@gmail.com",200)
print(john.toString())


