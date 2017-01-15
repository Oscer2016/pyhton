#tuxing4.py
#encoding=utf-8
n = input('请输入1个正整数n:')
for i in range(1,n+1):
        print ' '*(i-1),'*'*(2*(n-i)+1),' '*(i-1)
