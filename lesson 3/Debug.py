import datetime
time = datetime.datetime(2013,11, 2)
new_time = time.replace(month=int(time.month))

print(new_time)



