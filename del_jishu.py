#del_jishu.py
#encoding=utf-8
x = input('请输入一个由10个整数值构成的列表:')
for k in x:
    if k%2!=0:
        x.remove(k)
print x
