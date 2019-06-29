# append
nums = [1,2,3,4]
nums.append(5)
print(nums)
nums.append([6,7])

print(nums)

#clear方法
names =["Bill", "kevie", "Jack"]
print(names)
names.clear()
print(names)

#copy 方法
a =[1,2,3]
b = a
b[1] = 40
print(a)
print(b)

aa =[1,2,3]
bb = aa.copy()
bb[1]=90
print(aa)
print(bb)


#count 方法
search = ["he", "she", "he", "he", "she", "love"]
print(search.count("he"))
print(search.count("love"))


#extend方法
c= [1,2,3]
d = [4,5,6]
c.extend(d)
print(c)
print(d)


#index 方法
s = ["I","LOVE", "YOU"]
print(s.index("LOVE"))

#insert方法
numbers = [1,2,3]
numbers.insert(3,"four")
print(numbers)

#pop方法
numbers1 = [1,2,3]
print(numbers1.pop())
print(numbers1.pop(0))
print(numbers1)

#remove 方法
words = ["he", "she", "him", "her"]
print(words)
words.remove("he")
print(words)

#reverse 方法
numone = [1, 2, 3, 4]
numone.reverse()
print(numone)

#sort方法
numtwo = [5, 4, 7, 1, 8]
numtwo. sort()
print(numtwo)

x = [5, 4, 7, 1, 8]
y = x[:]
y.sort()
z = sorted(x)
print(x)
print(y)
print(z)


print(sorted("hellow"))

e = [3,4, 9, 8, 1, 2]
e.sort(reverse=True)    #降序排序
print(e)





