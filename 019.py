#Exp3_5.py
#encoding=utf-8
score=input('请输入你的成绩(0~100):')
if score<0 or score>100:
    print('无效的成绩')
elif score<60:
    print('不及格')
elif score<70:
    print('及格')
elif score<80:
    print('中等')
elif score<90:
    print('良好')
else:
    print('优秀')
