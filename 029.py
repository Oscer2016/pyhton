#Exp4_6.py
#encoding=utf-8
i=1
mu=0
s=0.0
n=int(raw_input('请输入n值:'))
while i <=n:
    mu+=i
    i+=1
    t=1.0/mu
    s+=t
print 's = ',s
