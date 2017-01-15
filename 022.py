#ques4_1.py
#encoding=utf-8
endFlag="yes"
sum=0.0
count=0
while endFlag[0]=='y':
    x=input("请输入一个分数：")
    sum=sum + x
    count=count + 1
    endFlag=raw_input("继续输入吗(yes or no)?")

print "\n平均分是：", sum / count
