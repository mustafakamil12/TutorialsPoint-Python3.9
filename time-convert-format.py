import datetime

format_time = '2021-04-27 01:02:01'
now = datetime.datetime.now()
print(f"now = {now}")

time_obj = datetime.datetime.strptime(format_time,'%Y-%m-%d %H:%M:%S')
time_string = datetime.datetime.strftime(time_obj,'%Y-%m-%d %H:00:00')

#time_string = now.strftime('%Y-%m-%d %H:00:00')



print("time_string: ", time_string)

#strptime(..).strftime('%Y-%m-%d %H:00:00')
