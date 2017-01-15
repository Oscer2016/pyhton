#yinzi.py
#encoding=utf-8
s = 0
n = input('请输入不大于1000的正整数n:')
for i in range(2,n,1):
    if n % i==0:
        s += i
print '它的所有因子（不包括1和该数本身）之和为',s
