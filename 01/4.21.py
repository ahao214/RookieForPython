spaceNum = 5
i = 1
lineSpaceNum = spaceNum
triangle = []

# 开始生成三角形

while lineSpaceNum >= 0:
    leftSpaceList = [' '] * lineSpaceNum
    startList = ['*'] * (2*i-1)
    rightSpaceList = [''] * lineSpaceNum
    lineList = leftSpaceList + startList + rightSpaceList
    triangle .append(lineList)
    lineSpaceNum -= 1
    i += 1
for line in  triangle:
    print(line)
