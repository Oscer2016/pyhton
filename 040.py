#Exp4_17.py
#encoding=utf-8
s = 0
print '200以内能被17整除的所有数是：'
for i in range(1,201):
    if i%17==0:
        print i,
        s += 1
print '\n数的个数是: ',s
