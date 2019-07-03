# 用同一个代码块处理多个异常

# 第一个自定义异常类
class CustomException1(Exception):
    pass

# 第二个自定义异常类
class CustomException2(Exception):
    pass


# 第三个自定义异常类
class CustomException3(Exception):
    pass

# 导入random模块
import random

# 随机抛出前面3个自定义异常
def raiseException():
    n = random.randint(1,3)     # 随机参数1到3的随机整数
    print("抛出CustomException{}异常".format(n))

    if n == 1:
        raise CustomException1
    elif n == 2:
        raise CustomException2
    else:
        raise  CustomException3

try:
    raiseException()
# 使用except字句同时捕捉这3个异常
except (CustomException1, CustomException2, CustomException3):
    print("执行异常处理程序")




