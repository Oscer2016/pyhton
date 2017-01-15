#Exp4_5.py
#encoding=utf-8
print '请输入若干字符，当输入#时则结束该操作'
while True:
    a= raw_input('请输入一个字符:')
    if a != '#':
        print '您输入的字符是:',a
    else:
        break
