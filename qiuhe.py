#qiuhe.py
#encoding=utf-8
print 'S=1+1/2+1/3+…+1/N'
S=0
mu=1
t=0
while S<=15:
    t = 1.0/mu
    mu += 1
    S += t
print 'S>15时最小N值',mu,',S=',S
