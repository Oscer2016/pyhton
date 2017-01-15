#grade.py
#encoding=utf-8
x = raw_input('请输入10个学生的成绩用逗号隔开:')
a = x.split(',')
b=[]
for k in a:
    b = b + [int(k)]
highest = max(b)
lowest = min(b)
aver = sum(b)*1.0/len(b)
print '最高分为',highest,'，最低分为',lowest,'，平均分为',aver,'。'

   
