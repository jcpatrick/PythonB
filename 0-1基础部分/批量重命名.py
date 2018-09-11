import os
#1获取要重命名的文件夹
dir_name = input("请输入文件夹名称：")
#2获取指定文件夹中的所有文件 名字
files_names = os.listdir(dir_name)
os.chdir(dir_name)#修改根目录
#3重命名
for name in files_names:
    print(name)
    os.rename(name,"[京东出品]-" + name)
