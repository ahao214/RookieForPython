from string import Template

template1 = Template("$s是我最喜欢的编程语言，$s学习很困难")
print(template1.substitute(s='python'))

template2 = Template("${s}stitute")
print(template2.substitute(s='sub'))

template3 = Template("$dollars$$相当于多少$pounds")
print(template3.substitute(dollars=20, pounds='英镑'))


template4 = Template("$dollar$$相当于多少$pounds")
data = {}
data["dollar"] = 100
data["pounds"] = "英镑"
print(template4.substitute(data))

s1 = "Today is {}, the temperature is {} degrees."
print(s1.format("Sunday", 34))

s2 = "Today is {week}, the temperature is {degree} degrees"
print(s2.format(degree = 23, week="Tus"))

fullname = ["Bill", "Gates"]
print("Mr {name[1]}".format(name=fullname))
print("first name is {name[0]}".format(name=fullname))


print("<" + "hello".center(30) + ">")
print("<{:^30}>".format("hello"))

print("<" + "hello".center(30, "*") + ">")
print("<{:*^30}>".format("hello"))

s = "hello world"
print(s.find("hello"))
print(s.find("love"))

print(s.find("l", 5, 9))

print(s.find("l",5, 10))

one = input("请输入一个大字符串：")
while True:
    subString = input("请输入一个子字符串：")
    if subString == "end":
        break
    startStr = input("请输入开始索引：")
    endStr = input("请输入结束索引：")
    start = 0
    end = len(s)

    if startStr != "":
        start = int(startStr)
    if endStr != "":
        end = int(endStr)

    print("'{}'在'{}'的出现的位置是{}:".format(subString, s, s.find(subString, start, end)))

