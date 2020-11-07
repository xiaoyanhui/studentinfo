import studb

if __name__ == '__main__':
    while True:
        print("""
==============================
学生管理系统V1.0
1.添加学生信息
2删除学生信息
3.修改学生信息
4.显示所有学生信息
0.退出系统
==============================
""")

        studb.create_table()
        op = int(input('请输入对应功能的数字'))
        while op < 0 or op > 4:
            op = int(input('请输入对应功能的数字'))
        if op == 1:
            studb.add_student()
        elif op == 2:
            studb.delete_stu()
        elif op == 3:
            studb.update_stu()
        elif op == 4:
            studb.search_stu()
        else:
            studb.imper1()
            break
        studb.imper()
