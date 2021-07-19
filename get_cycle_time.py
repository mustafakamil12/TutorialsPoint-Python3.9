import sys,os,re
import fileinput,subprocess,inspect,datetime
sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")
from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool
from datetime import datetime,date

#path = os.path.abspath(GFS_DBI.__file__)
#print(f"The GFS_DBI path is : {path}")
#dbh = GFS_DBI.initialise()

def get_cycle_time(timeArr):
   print("----get_cycle_time----")
   GFS_DBI.initialise()
   with CursorFromConnectionFromPool() as cursor:
      print(f"SELECT cycle_time from gfs_history limit 1;")
      cursor.execute(f"SELECT cycle_time from gfs_history limit 1;")
      row_ref = cursor.fetchall()
      row_ref_tup_to_list = []
      print("row_ref = ", row_ref)
      while row_ref:
         for elem in row_ref[0]:
            print("elem = ", elem)
            print("type(elem) = ", type(elem))
            if isinstance(elem, datetime):
               selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
               print("selem = ", selem)
               row_ref_tup_to_list.append(selem)
            else:
               row_ref_tup_to_list.append(elem)

         print("row_ref_tup_to_list: ", row_ref_tup_to_list)
         row_ref.pop(0)
         #row_ref_tup_to_list = []

      #print("row_ref: ", row_ref)
      if row_ref_tup_to_list:
         return row_ref_tup_to_list[0]
      else:
         return ""

official_tag = 'official'
official_history_column = 'official_table'
prod_send_update_column = 'product_send_time'

cycle_time_Arr = []
cycle_time_Arr.append(official_history_column)
cycle_time_Arr.append(official_tag)
print("cycle_time_Arr: ", cycle_time_Arr)
cycle_time_obj = get_cycle_time(cycle_time_Arr)

tickTub = cycle_time_obj[0]

print("tickTub: ", tickTub)
print("tickTub: ", type(tickTub))
