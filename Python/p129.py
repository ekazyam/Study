import datetime

today = datetime.datetime.now()

print today

print today.weekday()

if today.weekday() < 5:
	print ('OK')