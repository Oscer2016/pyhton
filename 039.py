#Exp4_16.py
#encoding=utf-8
x = input('请输入1个整数:')
for i in range(2,x):
    if x % i==0:
        break
if i==x-1:
    print x,'是个素数'
elif i<x-1:
    print x,'不是个素数'
