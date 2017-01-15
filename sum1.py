#sum1.py
#encoding=utf-8
import math
i = 1
t = 0
s = 0
n = input('请输入正整数n:')
while i <= n:
    m = math.sqrt(i)
    t += m
    s += t
    i += 1
print 'S =',s
