def add1(x,y,z):
    return  x + y + z

print(add1(1,2,3))

list=[2,3,4]
print(add1(*list))

dict = {'x':100,'y':200,'z':12}

print(add1(**dict))

# 用可变参数定义函数
def add2(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result
print(add2(1,2,3,4,5))

# 使用星号同样可以拆分列表
print(add2(*list))

# 定义add3函数时，numbers参数前面使用两个星号，表示这个参数值接收字典类型数据
def add3(**numbers):
    result = 0
    for item in numbers.items():
        # 将numbers字典中的所有value相加
        result += item[1]
    return result
# 将字典dict中的元素作为单独的参数传入了add3函数
print(add3(**dict))

# 定义一个只拥有普通形参的add4函数
def add4(numbers):
    result = 0
    for item in numbers.items():
        result += item[1]
    return result
print(add4(dict))






