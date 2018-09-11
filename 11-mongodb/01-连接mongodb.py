from pymongo import MongoClient

client = MongoClient("mongodb://py_test:123@192.168.1.13:27017/py_test",connect=False)
db = client['py_test']
stu= db.stu
datas = stu.find()

for data in datas:
	print(data.get("name"))
print("-----更新-----")
stu.update_one({"name":"cjc"},{'$set':{"age":28}})
datas = stu.find_one({"name":"cjc"})
print("%s----%s"%(datas['name'],datas['age']))
