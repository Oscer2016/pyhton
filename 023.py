#ques4_2.py
#encoding=utf-8
li=input('请输入一个列表:')
sum=0
for x in li:
    if x>0 and x%2==0:
        sum+=x
print 'sum=',sum
