#string.py
#encoding=utf-8
x = raw_input('请输一串字符串:')
a = list(x)
b = set(a)
for k in b:
    print k,',',a.count(k)
