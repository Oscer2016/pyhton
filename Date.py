#Date.py
#encoding=utf-8
x=input('请输入表示年月日的八位数：')
a=x//10000
b=(x-10000*a)//100
c=x-10000*a-100*b
print a,'年',b,'月',c,'日'
