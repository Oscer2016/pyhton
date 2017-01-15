#paixu.py
#encoding=utf-8
a,b,c = input('请输入三个数（用逗号隔开）:')
a_list = [a,b,c]
b = sorted(a_list,reverse=True)
print b[0],b[1],b[2]

