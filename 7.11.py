# 计算阶乘的递归函数
def jc(n):
    # 终止添加
    if n == 0 or n == 1:
        return 1
    else:
        # 进行递归调用
        return n * jc(n - 1)

# 计算10的阶乘
print(jc(10))

print("------------------")

# 计算斐波那契的递归函数
def fibonacci(n):
    # 终止条件
    if n == 1:
        return 0
    # 终止条件
    elif n == 2:
        return 1
    else:
        # 进行递归调用
        return fibonacci(n - 1) + fibonacci(n - 2)

# 斐波那契数列的第10个值
print(fibonacci(10))


