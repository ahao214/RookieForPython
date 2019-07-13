# 数据库表的查询操作
import  sqlite3
# 打开数据库
Con = sqlite3.connect("E:\sales.db")

# 创建游标对象
Cur = Con.cursor()

# 查询数据库表
Cur.execute("select id,price, name from book")
for row in Cur:
    print(row)
