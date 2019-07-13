import  sqlite3
books = [("021", 25, "大学计算机教学"),("022", 30, "大学英语"),("023", 14, "艺术欣赏"),("024", 55, "程序设计与艺术")]
# 打开数据库
Con = sqlite3.connect("E:\sales.db")
# 创建游标对象
Cur = Con.cursor()
# 插入一行数据
Cur.execute("insert into book(id,price,name) values ('001',33,'大学计算机')")
Cur.execute("insert into book(id,price,name) values(?,?,?)", ("002",34,"数据库教程"))
# 插入多行数据
Cur.executemany("insert into book(id,price,name) values (?,?,?)", books)

# 修改一条数据
Cur.execute("update book set price=? where name=?",(23, "大学英语"))
# 删除一行数据
n = Cur.execute("delete from book where price=?",(25,))
print("删除了", n.rowcount,"行记录")

Con.commit()
Cur.close()
Con.close()
