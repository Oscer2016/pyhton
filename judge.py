#judge.py
#encoding=utf-8
x = raw_input('请输入字符:')
if '0'<=x<='9':
  print '你输入的是数字'
elif 'a'<=x<='z' or 'A'<=x<='Z':
  print '你输入的是字母'
else:
  print '你输入的是其他字符'

