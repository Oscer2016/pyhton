#score sort:Exp2_2.py
#encoding=utf-8
studscore={"唐僧":45,"孙悟空":78,"猪八戒":40,"沙僧":96,"如来":65,"观音":90,"白骨精":78,"红孩儿":99,"太上老君":60,"白龙马":87}
maxscore=0
maxstudname=''
minscore=100
avrscore=0
studnum=len(studscore)

#输出所有成绩：
print("成绩分别为:")
for key in studscore.keys():
     print(key,studscore[key],"；",)

#换行
print

#进行成绩统计
for key in studscore.keys():
     if studscore[key]>maxscore:
           maxscore=studscore[key]
           maxstudname=key
     if studscore[key]<minscore:
           minscore=studscore[key]
           minstudname=key
     avrscore=avrscore+studscore[key]

avrscore=avrscore/studnum
print("全班共有",studnum,"人,平均成绩为:",avrscore,"分。")
print("最高分是：",maxstudname,maxscore,"分")
print("最低分是：",minstudname,minscore,"分")
