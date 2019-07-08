import time
localtime = time.localtime(time.time())
print('本地时间是：', localtime)
print('年：', localtime.tm_year)
print('月：',localtime.tm_mon)
print('日：', localtime.tm_mday)

print('一年的第%d天'%localtime[7])


