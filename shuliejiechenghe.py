#jiechengshuliehe.py
#encoding=utf-8
def f(n):
    if n!=1:
        return f(n-1)*n
    else:
        return n
s = 0.0
n = 1
while abs((-1)**(n-1)*1.0/f(n)) > 1e-6:
    zi = (-1)**(n+1)
    mu = f(n)
    n += 1
    t = zi*1.0/mu
    s += t
print 'S=',s
