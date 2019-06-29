# name = input("what is your name?")
# if name.startswith("Bill"):
#     if name.endswith("Gates"):
#         print("welcom Gates Bill")
#     elif name.endswith("Clinton"):
#         print("welcome CLinton Bill")
#     else:
#         print("unkonw name")
# elif name.startswith("ning"):
#     if name.endswith("li"):
#         print("welcome li")
#     else:
#         print("welcome ning")
# else:
#     print("unkonw name")


age = 4
assert 0 < age < 10
print("hello world")

x = 1
while x <= 5:
    print(x)
    x += 1
print("------------")
numbers = [1,2,3]
for number in numbers:
    print(number, end="")

print("------------")

for num in range(1,11):
    print(num,end="")





print("------------")

scope = {}
codes =""

print(">>>", end="")
while True:
    code = input("")
    if code == "":
        exec(codes, scope)
        codes =""
        print(">>>", end="")
        continue
    codes += code + "\n"


print("------------")









