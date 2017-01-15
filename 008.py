#Exp1_5.py
a=[[111,2,30],[4,50,6],[7,8,9]]
s1=''
print '______________1_______________'
for x in a:
     s=''
     for y in x:
           s1='%6d' % y
           s=s+s1
     print s
print '______________2_______________'
i=j=0
while i<3:
      j=0
      s=''
      while j<3:
            s1=str(a[i][j])
            s1=s+(s1+' '*(6-len(s1)))
            j=j+1
      print s
      i=i+1
print '\n用了两种方法\n'
            
