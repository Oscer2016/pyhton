#Ques1_2.py
#encoding utf-8
import math    #������ѧģ�飬�Ӷ�����ʹ��ģ���е���ѧ��������ѧ����
x=input('�������߼���н�(�ȣ� ���Զ��ŷָ���:')
a,b,sita=x
c=math.sqrt(a**2+b**2-2*a*b*math.cos(sita*math.pi/180))
print 'c='+str(c)
