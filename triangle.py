#Exp3_8.py
#encoding=utf-8
import math
a,b,c = input('请输入三角形三条边长(用逗号隔开):')
if a+b>c and a+c>b and b+c>a:
    #用海伦公式计算面积
    p = (a+b+c)/2.0
    temp=p*(p-a)*(p-b)*(p-c)
    area=math.sqrt(temp)
    if a==b==c:
        result='等边三角形'
    elif a==b!=c or a==c!=b or b==c!=a:
        result='等腰三角形'
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        result='直角三角形'
    else:
        result='普通三角形'
else:
    result='非三角形'
if result!='非三角形':
    print '面积:',area
print('三边构成: %s'%result)

