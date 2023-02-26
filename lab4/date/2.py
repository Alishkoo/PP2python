import datetime as dt

today = dt.date.today()
tomorrow = today - dt.timedelta(days=1)
yesterday = today - dt.timedelta(days=1)

print(today)
print(tomorrow)
print(yesterday)

