#Exp4_1.py
#encoding=utf-8
print '请输入若干正整数进行求和操作，当输入负数时结束:'
s = 0
x = input("请输入一个整数:")
while x>=0:
    s=s + x
    x = input("请输入一个整数:")
print '所有正整数之和=', s
