#Exp4_10.py
#encoding=utf-8
score = [70,90,78,85,97,94,65,80]
sum = 0
print '所有的分数值是:'
for i in range(len(score)):
    print score[i] ,
    sum += score[i]
aver = sum / 8.0
print '\naver=', aver
