#!/usr/bin/python3
#     Revision: 0.0.1     Modtime: 02/23/21 07:00 pm     Author: Mustafa Al Ogaidi
#
#   Python module:
#
#      GFS_date
#
#   Description:
#
#      Functions to which provide operations on "standard date" arrays.
#      a standard date array is defined as:
#          (minute, hour, day, month, year) where each entry
#      is an integer. For the month, January=1, February=2,...
#
#   Copyright (C) 2021, WSI Corporation
#
#   These coded instructions, statements, and computer programs contain
#   unpublished proprietary information of WSI Corporation, and are
#   protected by Federal copyright law.  They may not be disclosed
#   to third parties or copied or duplicated in any form, in whole or
#   in part, without the prior written consent of WSI Corporation.
#
#------------------------------------------------------------------------------

import time
import re

#
# Format a "standard date array" as a sql string.
#
def format_date(datearray):
    print("datearray: ", datearray)
    return str(datearray[4])+"-"+str(datearray[3])+"-"+str(datearray[2])+" "+str(datearray[1])+":"+str(datearray[0])+":00"

#
# Format a "standard date array as a compact tag string.
#
def format_date_tag(datearray):
    print("datearray: ", datearray)
    return str(datearray[4])+str(datearray[3])+str(datearray[2])+str(datearray[1])+str(datearray[0])

#
# Decode a SQL date string into a "standard date array".
#
def decode_sql_time(sqlDateString):
    print("sqlDateString: ", sqlDateString)
    pattern = r'([0-9][0-9]*)-([0-9][0-9]*)-([0-9][0-9]*) ([0-9][0-9]*):([0-9][0-9]*):([0-9][0-9]*)'
    decodeSqlTimeRegEx = re.compile(pattern)
    decodeSqlTimeValue = decodeSqlTimeRegEx.findall(sqlDateString)
    print(" Year , Mon , MDay , Hour , Min , Sec")
    return list(decodeSqlTimeValue[0])



#
# A utility routine which returns the number of days in a given month.
#
def days_in_month(myMonth, myYear):
    mon = int(myMonth)    
    year = int(myYear)

    if(mon == 2):
        if ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0)):
            days = 29
        else:
            days = 28
    elif(mon==6 or mon==4 or mon==9 or mon==11):
        days = 30
    else:
        days = 31

    return str(days)

#
#  Takes as inputs a stardard date array and an offset specified
# in minutes. It applies this offset to the input date and
#  returns the result in standard date array.
#
def add_date(min1, hour1, day1, mon1, year1, min_offset1):

    min = int(min1) 
    hour = int(hour1) 
    day = int(day1) 
    mon = int(mon1) 
    year = int(year1) 
    min_offset = int(min_offset1) 
    
    temp = int(min) + int(min_offset)

    if(temp >= 0):
        hour_offset = int(temp / 60)
    else:
        hour_offset = int((temp - 59) / 60)
    
    min = temp - hour_offset * 60
    temp = hour + hour_offset
    
    if (temp >= 0):
        day_offset = int(temp / 24)
    else:
        day_offset = int((temp - 23) / 24)
    
    hour = temp - day_offset * 24
    day = int(day) + day_offset
    
    while(1):
        if(day < 1):
            mon -= 1
            if(mon < 1):
                year -= 1
                mon = 12
            temp = int(days_in_month(mon,year))
            day = temp + day
        else:
            temp = int(days_in_month(mon, year))
            if(day <= temp):
                break
            day = day - temp
            mon += 1
            if (mon > 12):
                mon = 1
                year += 1

    return [min,hour,day,mon,year]


#
# Return the current date/time in standard date array form.
#
def current_date_time():
    cur_time = []
    obj_time = time.gmtime()
    cur_time.append(0)
    cur_time.append(obj_time.tm_min)
    cur_time.append(obj_time.tm_hour)
    cur_time.append(obj_time.tm_mday)
    cur_time.append(obj_time.tm_mon)
    cur_time.append(obj_time.tm_year)
    return cur_time[1:6]

#
# convert seconds since 1/1/70 into standard date array form.
#
def convert_date_time():
    cur_time = []
    obj_time = time.gmtime()
    cur_time.append(0)                  # [0] Pass 0 instead of secondes
    cur_time.append(obj_time.tm_min)    # [1] Pass Minutes
    cur_time.append(obj_time.tm_hour)   # [2] Pass Hours
    cur_time.append(obj_time.tm_mday)   # [3] Pass Day of Month
    cur_time.append(obj_time.tm_mon)    # [4] Pass Month
    cur_time.append(obj_time.tm_year)   # [5] Pass Year
    return cur_time[1:6]


#
# Executing Modules as Script.
#
if __name__ == "__main__":
    output = convert_date_time()
    print(output)
    strOutput = format_date(output)
    print(strOutput)
    print(format_date_tag(output))
    decodeSqlTime = decode_sql_time(strOutput)
    print(decodeSqlTime)
    print(days_in_month(decodeSqlTime[1],decodeSqlTime[0]))
    print(add_date(output[0], output[1], output[2], output[3], output[4], 5))
