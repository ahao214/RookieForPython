# 关键字参数和默认值

def sub1(m, n):
    return m - n

# 使用位置参数传递参数值
print(sub1(20, 4 ))

# 使用位置参数传递参数值
print(sub1(4, 20))

# 使用关键字参数传递参数值
print(sub1(m = 20, n = 4))

# 使用关键字参数传递参数值
print(sub1(n = 4, m = 20))


# 为sub2的两个参数指定默认值
def sub2(m = 100, n = 50):
    return m - n

# 调用sub2时未指定任何参数值
print(sub2())

# 调用sub2时使用了位置参数
print(sub2(45, 21))

# 调用sub2时使用了混合参数模式
print(sub2(53, n = 12))

# 调用sub2时使用了关键字参数，m仍然使用默认值
print(sub2(n = 123))

# 调用sub2时使用了关键字参数
print(sub2(m = 542, n = 143))

# 尽管关键字参数在位置参数后面使用，但产生了奇异，系统不知道m的值应该是53，还是12
print(sub2(53, m = 12))




