#1.py
while 1:
    x=raw_input()
    b=x.split()
    c=b[0]
    d=b[1]
    i=0
    n=1
    while 1:
        if c[:n]==d[:n]:
            i+=1
        else:
            break
        n+=1
    if i==0:
        print 'No common prefix'
    else:
        print 'The common prefix is',c[:i]
