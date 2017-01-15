#tuxing6.py
#encoding=utf-8
n = input('请输入1个正奇数n:')
for i in range(1,n+1):
    if i <= (n+1)/2:
        print ' '*(n-i),'*'*(2*i-1),' '*(n-i)
    else:
        print ' '*(i-1),'*'*(2*(n-i)+1),' '*(i-1)
