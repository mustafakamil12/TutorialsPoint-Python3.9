import sys,os,re
import fileinput,subprocess,inspect
sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")
from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool

#path = os.path.abspath(GFS_DBI.__file__)
#print(f"The GFS_DBI path is : {path}")

GFS_DBI.initialise()

with CursorFromConnectionFromPool() as cursor:
  cursor.execute('select * from timezones limit 10')  # here the email is inside tuple
  user_data = cursor.fetchall()  # this function is retrieve only one
  # return new object :)
  #print("email= " + user_data[1] + "first_name= " + user_data[2] + "last_name= " + user_data[3] + "id= " + user_data[0])
  print(user_data)
