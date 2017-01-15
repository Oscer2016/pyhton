#week.py
#encoding=utf-8
x = raw_input('请输入今天的星期：')
a = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
b = a.index(x)
c = 123456%7
print a[b+c]
