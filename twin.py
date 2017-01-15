#twin.py
#encoding=utf-8
a = []
n = 0
for i in range(101,201,2):
    for k in range(2,i):
        if i%k == 0:
            break
        if k==i-1:
            a = a + [i]
print '100~200之间的所有双胞胎素数：', 
while a[n+1]-a[n] == 2:
    print (a[n],a[n+1]),
    n += 1
    if a[n+1]-a[n] != 2:
        n+=1


