#multiply.py
#encoding=utf-8
m = 1
x = raw_input('请输入n个数（用逗号隔开）：')
a = x.split(',')
for k in a:
    if int(k)%2!=0:
	m *= int(k)
print m
