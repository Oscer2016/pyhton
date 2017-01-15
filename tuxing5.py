#tuxing5.py
#encoding=utf-8
n = input('请输入1个正奇数n:')
for i in range(1,n+1):
    if i <= (n+1)/2:
        print '*'*(2*i-1)
    else:
        print '*'*((n-i)*2+1)
        
