#Exp4_14.py
#encoding=utf-8
score = [50,40,20,30,10]
print '原始序列是：'
print(score)
a = len(score)
for i in range(a-1):
    min_score = score[i]
    k = i
    for j in range(i+1,a):
        if min_score > score[j]:
            min_score=score[j]
            k = j
    t = score[i]
    score[i]=score[k]
    score[k]=t
print '进行升序排列后的序列是：'
print score
        
