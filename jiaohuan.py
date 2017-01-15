#jiaohuan.py
#encoding=utf-8
for x in range(1,51):
    for y in range(1,51):
        for z in range(1,21):
            if x+y+z==50 and x+2*y+5*z==100:
                print '1分',x,'枚，2分',y,'枚，5分',z,'枚。'
