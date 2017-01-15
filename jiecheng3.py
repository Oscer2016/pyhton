#jicheng.py
def f(n):
    if n!=1:
        return f(n-1)*n
    else:
        return 1
n=input()
print f(n)
