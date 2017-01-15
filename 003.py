#Ques1_3.py
#encoding utf-8
r1,r2=input('请输入两只电阻的阻抗（以逗号分隔）：')
R=1.0/(1.0/r1+1.0/r2)
print('R='+'%6.2f' % R)
