import datetime as dt

def dt2_dt1(dt1, dt2):
    timedelta = dt2 - dt1
    return timedelta

dt1 = dt.datetime.today()
dt2 = dt.datetime.strptime('2024-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

print(dt2_dt1(dt1,dt2))
