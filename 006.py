#Exp1_3.py
s=input('x,y,z=')
x,y,z=s.split(',')#���ַ����ö��Ž��з��룬�����Ӵ����ɵ��б�
if x>y:
    x,y=y,x       #����x��y��ֵ
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print x,y,z
