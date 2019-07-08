import time
timeone = time.time()
timetwo = timeone + 60
print(timetwo)

time3 = timeone + 60 * 60
print(time3)

timeone = time.localtime(timeone)
timetwo = time .localtime(timetwo)
time3 = time.localtime(time3)

