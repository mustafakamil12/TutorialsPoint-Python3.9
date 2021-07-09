import calendar
import time
print("time.gmtime()", time.gmtime())
print(calendar.timegm(time.gmtime()))

myTimeArr = [59, 59, 23, 31, 11, 137, 3, 189, -1]
newTimeArr = [2012,6,1,12,0,0,4,153,-1]
targetArr = [2021, 7, 8, 18, 25, 14, 3, 189, 0]
print("myTimeArr = ", myTimeArr)
print(calendar.timegm(tuple(targetArr)))

"""
time.struct_time(tm_year=2012, tm_mon=6, tm_mday=1, tm_hour=12, tm_min=0,
tm_sec=0, tm_wday=4, tm_yday=153, tm_isdst=-1)

newTimeArr = [2012,6,1,12,0,0,4,153,-1]
"""
