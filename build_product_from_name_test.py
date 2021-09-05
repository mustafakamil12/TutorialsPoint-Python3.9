import psycopg2
import os
import subprocess

from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool


prod_list = ['HOURLYTRADERFC']
GFS_DBI.initialise()

def build_product_from_name(bpfnArr):
   print("----build_product_from_name----")

   prod_id = bpfnArr.pop(0)
   print("prod_id: ", prod_id)

   query = 'select format_descriptor_filename, station_list, ' + 'config_options, post_proc_script from ' + f"product where product_name = '{prod_id}'"
   print("query: ", query)

   with CursorFromConnectionFromPool() as cursor:
      cursor.execute(query)
      row_ref = cursor.fetchall()

   print("row_ref: ", row_ref)
   bpfiArr = []
   while row_ref:
      for elem in row_ref[0]:
          print(f"elem = {elem}")

          bpfiArr.append(elem)
      print("bpfiArr: ", bpfiArr)
      bpfiArr.insert(0,prod_id)
      print("bpfiArr: ", bpfiArr)
      #build_product_from_info(bpfiArr)

      row_ref.pop(0)
      bpfiArr = []


build_product_from_name(prod_list)
