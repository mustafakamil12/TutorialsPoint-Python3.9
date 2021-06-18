import time, subprocess, datetime

i = 1

dw_num = subprocess.run('date +%u',capture_output=True,text=True,shell=True)
#print("dw_num: ", dw_num)
subprocess_rc = dw_num.returncode
dw_num = dw_num.stdout
print("dw_num: ", dw_num)


cur_time = int(time.time())
des_time = cur_time - ((int(dw_num) - 1) * (3600 * 24))



start_week = des_time + ((7 * i ) * 24 * 3600)
print("start_week: ", start_week)
end_week = start_week + (6 * 3600 * 24)
print("end_week: ", end_week)

start_week = datetime.datetime.fromtimestamp(start_week)
end_week = datetime.datetime.fromtimestamp(end_week)

#output1 = time.strftime('%A %d-%b-%Y',start_week.localtime)
output1 = start_week.strftime('%A %d-%b-%Y')
#output2 = time.strftime('%A %d-%b-%Y',end_week.localtime)
output2 = end_week.strftime('%A %d-%b-%Y')

print("output1: ", output1)
print("output2: ", output2)


myLocalTime = time.localtime()
print(myLocalTime.tm_year,myLocalTime.tm_mon,myLocalTime.tm_mday,myLocalTime.tm_hour,myLocalTime.tm_min,myLocalTime.tm_sec)
Begindatestring = f"{myLocalTime.tm_year}-{myLocalTime.tm_mon}-{myLocalTime.tm_mday}"
print("Begindatestring = ", Begindatestring)

Begindate = datetime.datetime.strptime(Begindatestring, "%Y-%m-%d")
Enddate = Begindate + datetime.timedelta(days=300)
print("Begindate = ", Begindate)
print("Enddate = ", Enddate)
