#d2.py
#encoding=utf-8
import math
x1,y1=input('请输入第1个点x1,y1=')
x2,y2=input('请输入第2个点x2,y2=')
k=(y2-y1)/(x2-x1)
b=y1-k*x1
x3,y3=input('请输入第3个点x3,y3=')
d=abs(k*x3-y3+b)/math.sqrt(k**2+1)
print 'd=',d
