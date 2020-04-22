dict = {"name":"Bill", "age": 34, "sex":"男","salary":"4567"}
for key in dict:
    print(key, "=", dict[key], end=" ")
print()

for key, value in dict.items():
    print(key, "=", value, end=" ")
print()

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
for i in range(len(list1)):
    print("list1[" + str(i) + "]", "=", list1[i], "list2[" + str(i) + "]" , "=", list2[i], end=" ")
print()



dictone = {'a':1, 'b':2}
print(dictone)
dictone.clear()
print(dictone)


name1 ={"name":"Bill", "age":23}
name2 = name1
name1.clear()
print(name2)

dictinfo ={"name":"jace","age":23}
value = dictinfo.get('salary', 2345)
print(value)



