import pymysql
def select_list():
    """查询一个列表"""
    try:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="py_test")
        cursor = conn.cursor()
        sql ="select * from student"
        cursor.execute(sql)

        #获得列表结果
        result = cursor.fetchall()

        #判断并遍历结果集
        if result:
            for id,name,age in result:
                print("%d---%s---%d"%(id, name, age))

        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

def select_one():
    """查询一个列表"""
    try:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="py_test")
        cursor = conn.cursor()
        sql ='select * from student where id="2"'
        cursor.execute(sql)

        #获得列表结果
        result = cursor.fetchone()

        #判断并遍历结果集
        if result:
             print("%d---%s---%d"%result)


        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("--------列表-------")
    select_list()
    print("--------单列-------")
    select_one()



