#sushu.py
#encoding=utf-8
print '1~100之间的所有素数是：'
s = 1
print 2,
for i in range(1,101):
    for k in range(2,i):
        if i%k == 0:
            break
        if k == i-1:
            print i,
            s += 1
print '\n素数的个数是：',s
