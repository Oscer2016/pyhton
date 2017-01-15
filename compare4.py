#compare4.py
#encoding=utf-8
a,b,c,d = input('请输入4个数(用逗号隔开):')

#将前两个数从小到大顺序排列
if a>b:
    a,b = b,a
    
#将前三个数从小到大顺序排列    
if a>c:
    a,b,c = c,a,b
elif b>c:
    b,c = c,b
    
#将前四个数从小到大顺序排列
if a>d:
    a,b,c,d = d,a,b,c
elif b>d:
    b,c,d = d,b,c
elif c>d:
    c,d = d,c

#将这四个数按从小到大顺序输出
print '这4个数从小到大的顺序为:',a,b,c,d


    
