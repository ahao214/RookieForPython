# 数据库使用实例-学生通讯录
import  sqlite3
# 打开数据库
def opendb():
    conn = sqlite3.connect("E:\mydb.db")
    cur = conn.execute("create table if not exists tongxulu(usernum integer primary key,username varchar(128), password     varchar(128),address varchar(125), telnum varchar(128))")
    return cur, conn

# 查询全部信息
def showalldb():
    print("--------------------处理后的数据---------------------------")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxulu")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h)
        print
    cur.close()

# 输入信息
def into():
    usernum = input("请输入学号：")
    username1 = input("请输入姓名：")
    password1 = input("请输入密码：")
    address1 = input("请输入地址：")
    telnum1 = input("请输入联系电话：")
    return usernum,username1,password1,address1,telnum1

# 往数据库中添加内容
def adddb():
    welcome = "---欢迎使用添加数据功能---"
    print(welcome)
    person = into()
    hel = opendb()
    hel[1].execute("insert into tongxulu(usernum,username,password,address,telnum) values(?,?,?,?,?)", (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print("---恭喜你，数据添加成功---")
    showalldb()
    hel[1].close()

# 删除数据库中的内容
def deldb():
    welcome = "---欢迎使用删除数据库功能---"
    print(welcome)
    delchoice = input("请输入要删除的学号：")
    hel = opendb()
    hel[1].execute("delete from tongxulu where usernum="+ delchoice)
    hel[1].commit()
    print("---恭喜你，删除数据成功---")
    showalldb()
    hel[1].close()

# 修改数据库中的数据
def alter():
    welcome = "---欢迎使用修改数据库功能---"
    print(welcome)
    changechoise = input("请输入要修改的学生的学号：")
    hel = opendb()
    person = into()
    hel[1].execute("update tongxulu set usernum=?, username=?, password=?,address=?, telnum=? where usernum="+changechoise,(person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    showalldb()
    hel[1].close()

# 插叙数据
def searchdb():
    welcome ="---欢迎使用查询数据功能---"
    print(welcome)
    choice = input("请输入要查询的学生的学号：")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxulu where usernum="+choice)
    hel[1].commit()
    print("---恭喜你，你要查找的数据如下：---")
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    hel[1].close()

# 是否继续
def conti(a):
    choice = input("是否继续：（y or n）:")
    if choice == 'y':
        a = 1
    else:
        a = 0
    return a
if __name__=="__main__":
    flag = 1
    while flag:
        welcome="---欢迎使用数据库通讯录---"
        print(welcome)
        choiceshow="""
        请选择您的进一步选择
        (添加)往数据库里面添加内容
        (删除)删除数据库中的内容
        (修改)修改数据库中的内容
        (查询)查询数据库中的内容
        选择您想要进行的操作
        """
        choice = input(choiceshow)
        if choice =="添加":
            adddb()
            conti(flag)
        elif choice=="删除":
            deldb()
            conti(flag)
        elif choice=="修改":
            alter()
            conti(flag)
        elif choice=="查询":
            searchdb()
            conti(flag)
        else:
            input("你输入有误，请重新输入")