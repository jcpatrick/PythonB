from MyDbHelper import *
from hashlib import sha1

host = "127.0.0.1"
port = 3306
db_user = "root"
db_passwd = "root"
db_name = "py_test"
helper = None

def get_encrypted_passwd(passwd):
    s1 = sha1()
    s1.update(passwd.encode())
    return s1.hexdigest()

def check_user(user, passwd):
	helper = MyDbHelper(host,port,db_user,db_passwd,db_name)
	#校验用户信息
	sql = "select passwd from user where name=%s"
	db_user_passwd = helper.selectone(sql, [user])
	if not db_user_passwd:
		print("用户名错误")
	else:
		# 将密码进行sha1加密
		pwd = get_encrypted_passwd(passwd)
		if db_user_passwd[0] == pwd:
			print("登录成功")
			return True
		else:
		 print("密码错误")
	return False

def main():
	global helper
	helper = MyDbHelper(host,port,db_user,db_passwd,db_name)
	while True:
		user = input("请输入用户名：")
		passwd = input("请输入密码：")

		if user and passwd:
			#登录校验
			isChecked = check_user(user,passwd)
			if isChecked:
				break
			else:
				print("请重新输入登录信息")
	helper.close()

if __name__ == "__main__":
	main()
