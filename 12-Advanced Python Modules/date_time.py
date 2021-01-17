import datetime

mytime = datetime.time(21, 20, 3, 200)
print(mytime)
print(mytime.hour, mytime.min, mytime.second)
print(type(mytime))

today = datetime.date.today()
print(today)
print(today.year, today.month, today.day)
print(today.ctime())

mydatetime = datetime.datetime(2020, 1, 20, 21, 14, 40, 214)
print(mydatetime)

date1 = datetime.date(2021, 1, 10)
date2 = datetime.date(2020, 5, 15)
result = date1 - date2
print(type(result))
print(result)

mydatetime1 = datetime.datetime(2021, 1, 10, 21, 14, 40, 214)
mydatetime2 = datetime.datetime(2020, 1, 10, 15, 12, 20, 214)
resultdiff = mydatetime1 - mydatetime2
print(type(resultdiff))
print(resultdiff)
