#data sort Ques2_1.py
#coding=UTF-8
x1 = input('请输入第1个元素：')
x2 = input('请输入第2个元素：')           
x3 = input('请输入第3个元素：')
x4 = input('请输入第4个元素：')
x5 = input('请输入第5个元素：')


#将前2个元素按升序排列
if x1>x2:
     x1,x2=x2,x1


#将前3个元素按升序排列
if x1>x3:
     x1,x2,x3=x3,x1,x2
elif x2>x3:
      x2,x3=x3,x2


#将前4个元素按升序排列
if x1>x4:
     x1,x2,x3,x4=x4,x1,x2,x3
elif x2>x4:
     x2,x3,x4=x4,x2,x3
elif x3>x4:
     x3,x4=x4,x3


#将前5个元素按升序排列
if x1>x5:
     x1,x2,x3,x4,x5=x5,x1,x2,x3,x4
elif x2>x5:
     x2,x3,x4,x5=x5,x2,x3,x4
elif x3>x5:
     x3,x4,x5=x5,x3,x4
elif x4>x5:
     x4,x5=x5,x4

#输出排序结果
print "按升序排序结果为： ",x1,x2,x3,x4,x5
           
