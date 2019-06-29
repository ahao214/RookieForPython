# url = input("请输入一个url网站")
# scheme = url[0:5]
# host = url[8:]
# print("scheme:", scheme)
# print("host:", host)
#
# str = input("请输入一个整数")
# n = int(str)
# numbers = range(1, n)
# numbers1 = numbers[0::2]    #获取奇数
# numbers2 = numbers[1::2]    #获取偶数
# for num in numbers1:
#     print(num,end="")
# for num in numbers2:
#     print(num, end="")

print([1,2,3]+[4,5,6])

print("hello"+"world")

print([1,23] +["hello"])
print('hello' * 5)
print([10] * 2)
print("11" * 2)

str = "I love you"
print("you" in str)
print("I" in str)
print("Me" in str)
print("love" in str)

s = ["Bill", "Kevin", "Jack"]
print(s)
s[0] ="mary"
s[1] =20
print(s)


numbers = [1,2,3,4]
print(numbers)
del(numbers[2])
print(numbers)

names =["hello", "world", "yeon"]
names [1:] =["a", "b", "c"]
print(names)

name = list("Mike")
print(name)

nums =[1, 6, 7]
nums[1:1] = [2, 3, 4, 5]
print(nums)
nums[1:4] =[]
print(nums)
