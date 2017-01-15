#judgesushu.py
y = input()
x = y/2
if y == 1:
    print 'False'
else:
    while x>1:
        if y%x == 0:
            print 'False'
            break
        x-=1
    else:
        print 'True'
