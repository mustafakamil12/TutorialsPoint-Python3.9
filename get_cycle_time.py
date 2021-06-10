import sys,os,re

sys.path.append("/Users/mustafaalogaidi/Desktop/TWC/energy-pgs")


import fileinput,subprocess,inspect
import GFS_DBI
from GFS_DBI import CursorFromConnectionFromPool


dbh = GFS_DBI.initialise()

def get_cycle_time(timeArr):
   print("----get_cycle_time----")
   with CursorFromConnectionFromPool() as cursor:
      print(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      cursor.execute(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      ref = cursor.fetchall()
      print("ref: ", ref)
      if ref:
         return ref[0]
      else:
         return ""


official_tag = 'official'
official_history_column = 'official_table'
prod_send_update_column = 'product_send_time'

cycle_time_Arr = []
cycle_time_Arr.append(official_history_column)
cycle_time_Arr.append(official_tag)
print("cycle_time_Arr: ", cycle_time_Arr)

cycle_time = get_cycle_time(cycle_time_Arr)

print("cycle_time: ", cycle_time)
