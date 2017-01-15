#Exp1_2.py
import datetime
today=datetime.date.today()
one=datetime.timedelta(days=1)
yestoday=today-one
tomorrow=today+one
print yestoday,today,tomorrow
