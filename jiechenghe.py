#jiechenghe.py
#encoding=utf-8
def f(i):
    if i!=1:
        return f(i-1)*i
    else:
        return i
s = 0
i = input('请输入一个正整数:')
while i>0:
    t = f(i)
    s += t
    i -= 1
print s


