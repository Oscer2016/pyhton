#Exp1_3.py
s=input('x,y,z=')
x,y,z=s.split(',')#把字符串用逗号进行分离，返回子串构成的列表
if x>y:
    x,y=y,x       #交换x，y的值
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print x,y,z
