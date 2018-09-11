class Mouse:
    '''声明一个类'''
    #初始化对象，会被自动调用
    def __init__(self,new_name,new_age):
        print("init...")
        self.name = new_name
        self.age = new_age
    #__str__()方法,用于获取对象信息,没有该方法的话print(对象)时返回的是内存地址
    def __str__(self):
        return "%s is %d years old!"%(self.name,self.age)
    #方法
    def dance(self):
        print("dancing")
    def jump(self):
        print("jumping")
    def introduce(self):
        #当name、age属性没被添加时会报AttributeError
        print("name:%s,age=%d" % (self.name, self.age))

mikey = Mouse("Mikey",19)#创建一个对象
#mikey.introduce()

mikey.dance()
mikey.jump()

#添加属性
# mikey.age = 19
# mikey.name = "mikey"

# print("name:%s,age=%d"%(mikey.name,mikey.age))
mikey.introduce()
print(mikey)#输出对象信息