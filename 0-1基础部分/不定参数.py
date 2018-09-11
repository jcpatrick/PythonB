#*args传入的是一个元祖
def print_args(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)


#**kwargs传入的是一个字典dict

def print_args2(a,b,c=0,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

print_args(123,321,222,444,555)
print_args2(12,22,33,444,name="zd",age=50)

A = (44,55,66)
B = {"name" : "abc","age" : 15}
#当想将元祖和字典传入方法的可变参数时，元祖可以在前面加*，而字典则加**，表示拆包
print_args2(11,22,33,*A,**B)
t