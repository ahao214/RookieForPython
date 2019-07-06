# 生成器
# 定义一个生成器函数
def myGenerator():
    numList = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in numList:
        # yield语句会冻结当前函数，并提交当前要生成的值
        yield num
# 对生成器进行迭代
for num in myGenerator():
    print(num, end=' ')

print("------------------------")



# 利用生成器将一个二维的类别转换为一维的列表
nestedList = [[1, 2, 3], [4, 3, 2], [1, 2, 4, 6, 7]]
def enumList(nestedList):
    # 对二维的列表进行迭代
    for subList in nestedList:
        # 二维列表中每一个元素是一个一维的列表，所以需要对一维的列表进行迭代
        for element in subList:
            yield element

# 对生成器函数进行迭代
for num in enumList(nestedList):
    print(num, end=' ')
print()

# 将生成器函数转换为列表
numList = list(enumList(nestedList))
print(numList)
print(numList[1:4])



