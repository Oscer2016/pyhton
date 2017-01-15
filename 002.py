#Ques1_2.py
#encoding utf-8
import math    #导入数学模块，从而可以使用模块中的数学函数和数学常量
x=input('输入两边及其夹角(度） （以逗号分隔）:')
a,b,sita=x
c=math.sqrt(a**2+b**2-2*a*b*math.cos(sita*math.pi/180))
print 'c='+str(c)
