import datetime
import time

date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

print("time.time() = ", time.gmtime(time.time()))

print("time() = ", time.time())

#datetime.fromtimestamp(timestamp)

build_time = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time()))
print(build_time)

now = datetime.datetime.now()

elapsed = "%02d:%02d" % (now.minute,now.second)
print("elapsed: ", elapsed)
