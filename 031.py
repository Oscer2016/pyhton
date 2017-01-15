#Exp4_8.py
#encoding=utf-8
i=1
print '1~100之间能被7整除，但不能同时被5整除的所有数：'
while i<=100:
    if i % 7==0 and i % 5 != 0:
        print i,'\t',
    i+=1
    
