#function.py
#encoding=utf-8
import math
a,b,c = input('请输入系数（用逗号隔开）:')
if b**2-4*a*c >= 0:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print 'x1=',x1,'x2=',x2
else:
    print '此方程无实数解'
