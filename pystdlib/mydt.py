import datetime 
now = datetime.datetime.now()
print(now,type(now))
print(now.strftime('%Y%m%d%H%M%S'))
print(datetime.MAXYEAR,type(datetime.MAXYEAR))

td1 = datetime.timedelta(minutes=1)
print(td1,td1.total_seconds())

today1 = datetime.date.today()
print(today1,type(today1))
print(today1.year)
print(today1 - datetime.timedelta( days = 20))
print(today1.toordinal())
print(today1.isoformat())
print(today1.timetuple()) 


today2 = datetime.datetime.today()
print(today2.isoformat())
print(today2.timetz())
print(today2.tzname())

 