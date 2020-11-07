import sqlite3

connect = sqlite3.connect('student.db')  # 打开一个本地数据库用来存储信息
cx = connect.cursor()  # 获取游标对象用来执行SQL语句


# 构造一个数据表用于存放数据
def create_table():
    """
    使用create table if not exists student来判断数据库中是否存在一张student的数据表，
    不存在则创建一张数据表，
    若存在则不进行创建
    """
    create_sql = 'create table if not exists student(id INTEGER PRIMARY KEY UNIQUE ,name TEXT,sex TEXT,phone TEXT)'
    cx.execute(create_sql)


# 构造一个统计数据表中所有的学生信息
def count_total_stu():
    total_sql = 'select count(*) from student'
    res = cx.execute(total_sql)
    result = res.fetchone()[0]
    return result


# 构造一个用于添加学生信息的函数
def add_student():
    name = input('请输入新学生的名字:')
    sex = input('请输入新学生的性别:(男/女)')
    phone = input('请输入新学生的手机号码')
    add_sql = "insert into student(name ,sex,phone) values ('%s','%s','%s')" % (name, sex, phone)
    cx.execute(add_sql)


# 构造一个查询指定学生的函数
def appoint_stu(number):
    appoint_sql = "select * from student where id=%d" % number
    res = cx.execute(appoint_sql)  # 获取执行sql语句并返回的结果
    result = res.fetchone()  # 返回一条记录
    return len(result)


# 构造一个查询所有学生信息
def search_stu():
    count = count_total_stu()
    if count != 0:
        search_sql = 'select * from student'
        result = cx.execute(search_sql)
        print("""序号    姓名    性别     手机号码""")
        for id, name, sex, phone in result:
            print(id, '   ', name, '   ', sex, '    ', phone)
    else:
        print('没有学生信息，无法查询')


# 构造一个用于删除学生信息
def delete_stu():
    count = count_total_stu()
    if count != 0:
        print("""
=============================
1.删除指定学生的信息
2.删除所有学生的信息
=============================
""")
        search_num = int(input('请输入对应功能的数字:'))
        while search_num != 1 and search_num != 2:
            search_num = int(input('请正确的输入对应动能的数字:'))
        if search_num == 1:
            search_stu()
            search_num1 = int(input('请输入要删除学生信息的序号:'))
            while not appoint_stu(search_num1):
                search_num1 = int(input('请输入要删除学生信息的正确序号:'))
            delete_sql = "delete from student where id=%d" % search_num1
        else:
            delete_sql = 'delete from student'
        cx.execute(delete_sql)
    else:
        print('没有学生信息无法进行删除')


# 构造一个修改学生信息
def update_stu():
    count = count_total_stu()
    if count != 0:
        search_stu()
        update_num = int(input('请输入要修改学生信息的序号:'))
        while not appoint_stu(update_num):
            update_num = int(input('请输入要修改学生信息的正确序号:'))
        new_name = input('请输入新学生的名字:')
        new_sex = input('请输入新学生的性别:(男/女)')
        new_phone = input('请输入新学生的手机号码:')
        update_sql = "update student set name='%s',sex='%s',phone='%s' where id=%d" % (new_name, new_sex, new_phone, update_num)
        cx.execute(update_sql)
    else:
        print('没有学生信息无法进行修改')


# 构造一个提交数据的方法
def imper():
    connect.commit()


# 构造一个推出系统后关闭cursor获取游标和关闭数据库连接
def imper1():
    cx.close()
    connect.close()