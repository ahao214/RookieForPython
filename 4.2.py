months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
year = input("年：")
month = input("月(1-12)：")
day = input("日(1-31)：")
monthNumber = int(month)
monthName = months[monthNumber - 1]
print(year + "年" + monthName + day + "日")




