#Pi.py
#encoding=utf-8
i = 1
t = 1.0
s = 0.0
while abs(t) > 1e-6:
    s += t
    zi = (-1)**i
    mu = 2 * i + 1
    t = zi*1.0 / mu
    i += 1
print 'Pi =',4*s
    
    
    
    
    
