import string
list = ['a','b', 'c', 'd']
s = "+"
print(s.join(list))

print("1+2+3+4".split("+"))

listone = '/usr/local/nginx'.split('/')
print(listone)
print("c:" + "\\".join(listone))
print("i like python".split())
print("HELLO".lower())
print("world".upper())
eng = ["Python", "Ruby", "Java", "KONNN"]
if "Java" in eng:
    print("找到了java")
else:
    print("没有找到java")

for lang in eng:
    if "Java" == lang.lower():
        print("找到了java")
        break

one = "i like you, but you don't like me "
print(string.capwords(one))
