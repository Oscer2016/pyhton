#score count:Exp2_1.py
score=[68,75,32,99,78,45,88,72,83,78]
a=0
b=0
c=0
d=0

#输出所有成绩
print "成绩分别为:",
for s in score:
   print s,

#换行
print

#对成绩进行分段统计
for s in score:
      if s<60:
            d=d+1
      elif s<80:
            c=c+1
      elif s<90:
            b=b+1
      else:
            a=a+1
print "分段统计结果：优",a,"人,良",b,"人,中",c,"人,差",d,"人"
