#year.py
#encoding=utf-8
x = input('请输入年份:')
if x%400==0:
    print '你输入的年份是闰年'
elif x%4==0 and x%100!=0:
    print '你输入的年份是闰年'
else:
    print '你输的年份不是闰年'
