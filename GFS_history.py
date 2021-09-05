#!/usr/bin/python3
#     Revision: 0.0.1     Modtime: 03/09/21 09:00 am     Author: Mustafa Al Ogaidi
#
#   Python module:
#
#      GFS_history
#
#   Description:
#
#      Functions to access the gfs_history table
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

import sys,os,re
import fileinput,subprocess,inspect,datetime

from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool
from datetime import datetime,date





def get_cycle_time(timeArr):
   print("----get_cycle_time----")
   GFS_DBI.initialise()
   with CursorFromConnectionFromPool() as cursor:
      print(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      cursor.execute(f"SELECT cycle_time from gfs_history where {timeArr[0]} = '{timeArr[1]}';")
      #print(f"SELECT cycle_time from gfs_history limit 1;")
      #cursor.execute(f"SELECT cycle_time from gfs_history limit 1;")
      row_ref = cursor.fetchall()
      row_ref_tup_to_list = []
      while row_ref:
         for elem in row_ref[0]:
            if isinstance(elem, datetime):
               selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
               row_ref_tup_to_list.append(selem)
            else:
               row_ref_tup_to_list.append(elem)

         print("row_ref_tup_to_list: ", row_ref_tup_to_list)
         row_ref.pop(0)
         #row_ref_tup_to_list = []

      #print("row_ref: ", row_ref)
      if row_ref_tup_to_list:
         print("row_ref_tup_to_list[0] = ", row_ref_tup_to_list[0])
         return row_ref_tup_to_list[0]
      else:
         print("Nothing to return ...")
         return ""


def remove_history_row(histArr):

   with CursorFromConnectionFromPool() as cursor:
      cursor.execute(f"delete from gfs_history where cycle_time = '{histArr[0]}';")


def notify_history():

   with CursorFromConnectionFromPool() as cursor:
      cursor.execute('notify gfs_history;')

def add_history_row(histArr):

   with CursorFromConnectionFromPool() as cursor:
      cursor.execute(f"insert into gfs_history values ('{histArr[0]}', '{histArr[1]}');")

   notify_history()

def update_history_row(histArr):
   print("histArr: ", histArr)

   if histArr[0] != '' and histArr[0] != None:

      with CursorFromConnectionFromPool() as cursor:
         print(f"update gfs_history set {histArr[1]} = '{histArr[2]}' where cycle_time = '{histArr[0]}';")
         cursor.execute(f"update gfs_history set {histArr[1]} = '{histArr[2]}' where cycle_time = '{histArr[0]}';")

      notify_history()


if __name__ == "__main__":
   official_tag = 'official'
   official_history_column = 'official_table'
   prod_send_update_column = 'product_send_time'

   cycle_time_Arr = []
   cycle_time_Arr.append(official_history_column)
   cycle_time_Arr.append(official_tag)
   cycle_time = get_cycle_time(cycle_time_Arr)
   print("cycle_time = ", cycle_time)
