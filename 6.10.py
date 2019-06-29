dict = {'c':10, 'a':40, 'b':12, 'x':44}
dict['g'] = 3
dict['j'] = 3
print(dict.pop('b'))
for i in range(len(dict)):
    print(dict.popitem())

dict1 = {"a":1, "b":2, "c":3}
print(dict1.values())
for value in dict1.values():
    print(value)
print("-----------")
for key in dict1.keys():
    print(key)




