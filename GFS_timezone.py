import sys,os,re
import fileinput,subprocess,inspect
from datetime import datetime
from GFS_time import *
from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool


def get_timezone_offset(timeArr,timezone_cache=[]):
   utc_time_ref=timeArr.pop(0)
   utc_time=utc_time_ref
   timezone_code=timeArr.pop(0)

   if len(timezone_code) == 0:
      return(0)

   # first check to see if we have cached an entry for this zonecode/time
   for i in range(0,(len(timezone_cache)-1)):
      cache_ref = timezone_cache[i]
      start_time_ref = cache_ref[1]
      end_time_ref=cache_ref[2]
      if cache_ref[0] == timezone_code and utc_time.seconds_after(start_time_ref) >= 0 and utc_time.seconds_after(end_time_ref) <= 0:
         return(cache_ref[3])

   utc_time_text=utc_time.strftime('%Y-%m-%d %H:%M:%S')
   query='select start_time, end_time, utc_offset, abbrev, isdst from ' + 'timezones ' + f"where timezone_code = '{timezone_code}' " + f" and start_time <= '{utc_time_text}' " + f" and end_time >= '{utc_time_text}' "

   print(query)

   dbh = GFS_DBI.initialise()
   if dbh == None:
      print("Could not connect to database server")

   with CursorFromConnectionFromPool() as cursor:
      cursor.execute(query)
      row_ref = cursor.fetchall()

   s_idx=0
   info_idx=0

   if row_ref:
      start_time = GFS_time(row_ref[0])
      end_time = GFS_time(row_ref[1])
      abbrev = row_ref[3]
      #abbrev = str.replace(' *$',' *$',1)
      abbrev.rstrip()
      record_ref = [timezone_code,start_time,end_time,row_ref[2],abbrev,row_ref[4]]
      timezone_cache.append(record_ref)
      return(row_ref[2])
   else:
      return(0)
