# 没有返回值的函数

def test (flag):
    print("这是在函数中打印的信息")
    if flag:
        return
    print("这行信息只有在flag为False时才会输出")

# flag参数值为False，会输出最后一行信息
test(False)
print("--------")

# 调用test函数，flag参数值为True，最后一行信息不回输出
returnValue = test(True)
# 输出最后一行信息
print(returnValue)


