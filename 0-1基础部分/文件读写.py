# f = open("aaa.py","r+")
# f.write("hello")
# f.close()

#文件复制
old_file_name = "test.txt"
f_old = open(old_file_name,"r",encoding="UTF-8")
index = old_file_name.rfind(".")#找到右边的.号
new_file_name = old_file_name[:index] + "[复件]" + old_file_name[index:]

f_new = open(new_file_name,"w",encoding="UTF-8")
while True:
    content = f_old.read(1024)#每次制度1024个字节
    if len(content) == 0:
        break
    f_new.write(content)
f_new.close()
f_old.close()