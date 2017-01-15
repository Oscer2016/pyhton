#Exp4_11.py
#encoding=utf-8
score = [70,90,78,85,97,94,65,80]
max_score=score[0]
min_score=score[0]
print '所有的分数值是:'
for i in score:
    print(i) ,
    if i > max_score:
        max_score=i
    if i < min_score:
        min_score=i

print '\n'
print '最高分 = ',max_score
print '最低分 = ',min_score
