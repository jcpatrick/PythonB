import pymysql
class MyDbHelper(object):
    def __init__(self, host, port, username, password, db_name, charset="utf-8"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
        self.charset = charset
        self.conn = None

    def create_connection(self):
        """创建连接"""
        if not self.conn:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, db=self.db_name)

    def executesql(self, sql, param):
        self.create_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, param)
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
    def close(self):
        if self.conn:
            self.conn.close()
    def selectone(self, sql, param):
        self.create_connection()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, param)
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()

    def selectall(self, sql, param):
        self.create_connection()
        c = self.conn.cursor()
        try:
            c.execute(sql, param)
            result= c.fetchall()

            c.close()
            return result
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    sql = "select * from student"
    helper = MyDbHelper("127.0.0.1", 3306, "root", "root", "py_test")
    result = helper.selectall(sql, [])
    print(str(result))

    sql1 = "select * from student where name=%s"
    param1 =[ "cjc"]
    result = helper.selectone(sql1, param1)
    print(str(result))




