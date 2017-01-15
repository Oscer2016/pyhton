#sum2.py
mu= 1.0
i = 1
s = 0.0
while i <= 50:
    mu*= i
    i += 1
    t = 1.0/mu
    s += t
print 'S =',s
