#guess.py
#encoding=utf-8
x = 123
y = input('请输入整数:')
while x!=y:
  if x<y:
    print '太大'
    y = input('请输入小一点的整数:')
  else:
    print '太小'
    y = input('请输入大一点的整数:')
else:
   print '正确'
