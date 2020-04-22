# 可变参数

# 定义addNumbers函数，该函数指定了一个可变参数numbers
def addNumbers(*numbers):
    result = 0
    # 枚举numbers中的所有参数值，并将这些值累加，存储到result变量中
    for number in numbers:
        result += number
    # 返回累加值
    return  result

# 调用addNumbers函数
print(addNumbers(1,2,3,4,5))
print("-----")


# 定义calculator函数，在可变参数numbers前面加了一个普通的形参type
def calculator(type, *numbers):
    result = 0
    # type参数的值可为add、sub、mul和div，分别表示加、减、乘、除

    # 进行加法运算
    if type == "add":
        for num in numbers:
            result += num

    # 减法运算
    elif type == "sub":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]

    # 乘法运算
    elif type == "mul":
        result = 1
        for number in numbers:
            result *= number

    # 除法运算
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]

    # 返回计算结果
    return result;

print(calculator("add",1,2,3,4,5))

print(calculator("sub",1234, 44, 54, 12, 57))

print(calculator("mul",1,2,3,4,5,6,7))

print(calculator("div",100, 2, 5))

print("________________")

# 定义calculator1函数，在可变参数numbers后面指定了一个普通的形参ratio
def calculator1 (type,*numbers,ratio):
    # 在调用另一个函数时，如果为该函数的可变参数传入另一个可变参数值，也要在参数名前面加星号(*)
    return calculator(type, *numbers) * ratio

print(calculator1("add",1,2,3,4,5,6,ratio= 3))

print(calculator1("sub",1234,44,54,12,57,ratio=2))

print(calculator1("mul",1,2,3,4,5,6,7,ratio=4))

print(calculator1("div",100,2, 5,ratio=4))


# 定义calculation2函数，为ratio参数指定一个默认值4
def calculation2(type,*numbers, ratio = 4):
    return calculator(type,*numbers) * ratio

print(calculation2("add",1,2,3,4,5,6))

