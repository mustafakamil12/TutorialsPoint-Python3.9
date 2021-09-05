import sys,os,re
import fileinput,subprocess,inspect,datetime
import GFS_DBI
from GFS_DBI import CursorFromConnectionFromPool

"""
dbh = GFS_DBI.initialise()
if dbh == None:
    sys.exit('Could not connect to database server\n')
"""
GFS_DBI.initialise()

def get_cycle_time(timeArr):
   print("----get_cycle_time----")
   with CursorFromConnectionFromPool() as cursor:
      print(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      cursor.execute(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      row_ref = cursor.fetchall()
      row_ref_tup_to_list = []
      while row_ref:
         for elem in row_ref[0]:
            if isinstance(elem, datetime.date):
               selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
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

cycle_time_Arr = ['official_table', 'official']

print(get_cycle_time(cycle_time_Arr))
