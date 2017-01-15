#len.py
#encoding=utf-8
z = 0
f = 0
l = 0
x = raw_input('请输入n个数（用逗号隔开）:')
a = x.split(',')
for k in a:
    if int(k)>0:
	z += 1
    elif int(k)<0:
	f += 1
    else:
	l += 1
print '正数个数：',z,'负数个数：',f,'零的个数：',l
