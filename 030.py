#Exp4_7.py
i=1
zi=1.0
mu=1.0
t=1.0
s=0.0
while t >=1e-8:
    s = s + t
    zi = zi * i
    mu = mu * (2 * i + 1)
    t = zi * 1.0 / mu
    i+=1
print 'PAI = ', (2 * s)
