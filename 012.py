#score count:Exp2_1.py
score=[68,75,32,99,78,45,88,72,83,78]
a=0
b=0
c=0
d=0

#������гɼ�
print "�ɼ��ֱ�Ϊ:",
for s in score:
   print s,

#����
print

#�Գɼ����зֶ�ͳ��
for s in score:
      if s<60:
            d=d+1
      elif s<80:
            c=c+1
      elif s<90:
            b=b+1
      else:
            a=a+1
print "�ֶ�ͳ�ƽ������",a,"��,��",b,"��,��",c,"��,��",d,"��"
