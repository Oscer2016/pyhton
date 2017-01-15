#Exp4_12.py
#encoding=utf-8
s = 0.0
n = int(raw_input('请输入n值:'))
for i in range(1,n+1):
    s += 1.0 / i
print '1+1/2+…+1/',n, '=', s
