dict1 = {'title':'lph学院',
         'website':'https://www.lph.com',
         'des':'从事在线IT教育'
         }
dict2 = {
'title':'lph学院',
         'products':['lph学院','博客','微博','短信服务'],
         'des':'从事在线IT教育'
}

dict1.update(dict2)
for item in dict1.items():
    print("key = {key} value = {value}".format(key = item[0], value = item[1]))



