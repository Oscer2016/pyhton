#value.py
#encoding=utf-8
a_list = [ ]        #初始化一个空列表

x = input('请输入1个值:')
while x != 0:
        a_list=a_list + [x]
        x = input('请输入1个值:')
else:
        print a_list
