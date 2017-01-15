#string.py
i = 0
while True:
    x = raw_input()
    x = x.split()
    while x[0][i]==x[1][i]:
        i+=1
        a=x[0]
    if x[0][0]!=x[1][0]: 
        print 'No common prefix'
    elif i>0:
        print 'The common prefix is',a[:i]
