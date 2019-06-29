def fibs(n) :
    # 定义保存斐波那契数列的出事列表
    result = [0, 1]
    # 通过循环来计算斐波那契数列，并将计算结果保存到result列表中
    for i in range(n - 2):
        result.append(result[-2] + result[-1])
    return result


while True:
    value = input("请输入一个整数")

    if value == ":exit":
        break ;
    n = int(value)
    print(fibs(n))



