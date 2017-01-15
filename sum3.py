#sum3.py
#encoding=utf-8
mu= 1.0
i = 1
t = 1.0
s = 0.0
n = input('请输入正整数n:')
x = input('请输入x:')
while i <= n:
    s += t
    zi = x ** i
    mu*= i    
    t = (zi*1.0)/mu
    i += 1
print 'S =',s
