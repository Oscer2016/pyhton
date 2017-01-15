#Exp4_9.py
#encoding=utf-8
i=100
print '所有水仙花数是:'
while i<=999:
    bai = i / 100
    shi = (i % 100) / 10
    ge = i % 10
    if bai ** 3 + shi ** 3 + ge ** 3==i:
        print i,'\t',
    i+=1
