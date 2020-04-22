dict = {}
dict[20] = "Bill"
dict["Mike"] = {'age':30, "salary":3000}
dict[(12, "Mike", True)] = "hello"
print(dict)


IDES = {
    'eclipse':
        {
            'language':['Jave', 'Python', 'JavaScript', 'PHP'],
            'organization':'E基金会'
        },
    'visualstudio':
        {
            'language':['C#', 'C++', 'VB.NET'],
            'organization': '微软'
        },
    'webstorm':
        {
            'language':[ 'JavaScript'],
            'organization':'Jeb'
        }
}
labels = {
    'language':'支持的编程语言',
    'organization':'所属机构'
}

IDE = input("请输入IDE名字：")
findIDE = IDE.replace(" ","").lower()
choice = input("要查询IDE支持的编程语言(lang)还是所属机构组织(org)?")
if choice =="lang": key ='language'
if choice =="org": key ='organization'

if findIDE in IDES:
    print("{}{}是.".format(IDE, labels[key], IDES[findIDE][key]))
    


