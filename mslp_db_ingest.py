import sys,os
sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")
import GFS_time
from GFS_time import *


# Time/Date Strings
today = GFS_time([])
yyyy = today.as_text('%Y')
mm = today.as_text('%m')
dd = today.as_text('%d')
yyyymmdd = yyyy + mm + dd
inputdate = f"{yyyy}-{mm}-{dd}"

print(f"today = {today}")
print(f"yyyy = {yyyy}")
print(f"mm = {mm}")
print(f"dd = {dd}")
print(f"yyyymmdd = {yyyymmdd}")
print(f"inputdate = {inputdate}")

validtime = GFS_time(f"{inputdate} 00:00:00")
print(f"validtime = {validtime}")
initstring = today.as_text('%Y') + '-' + today.as_text('%m') + '-' + today.as_text('%d') + ' ' + today.as_text('%H:%M:%S')

param_code = 19
fcst_source =3

print(f"validtime = {validtime}")
# Read the forecast file
fcst_dir = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
fcst_file = f"{fcst_dir}/mslp.txt"

rowdata = []
numstations = 0
hournum = 0
id = []
data = []
pmslRow = []
pmsl = []
s = 0
i = 0


try:
   FCSTFILE = open(f"{fcst_file}",'r')
except OSError as error:
    print(f"Got error = {error}")
    sys.exit()

FCSTFILE_lines = FCSTFILE.readlines()
#print(f"FCSTFILE_lines = {FCSTFILE_lines}")
#print(len(FCSTFILE_lines))
#print(f"FCSTFILE_lines[0] = {FCSTFILE_lines[0]}")
#print(f"length of FCSTFILE_lines = {FCSTFILE_lines}")
while FCSTFILE_lines:
    rowdata = FCSTFILE_lines[0].split(' ')
    i = 0
    for rowd in rowdata:
        rowd = rowd.replace("\n","")
        data.append(rowd)
        i += 1

    #print(f"data = {data}")
    id.insert(s,data.pop(0))
    pmsl.insert(s,data)
    FCSTFILE_lines.pop(0)
    s += 1
    data = []
#print(f"pmsl = {pmsl}")
numstations = s - 1
numhours = i - 1
FCSTFILE.close()

#print(f"s = {s}")
#print(f"i = {i}")
#print(f"numstations = {numstations}")
#print(f"numhours = {numhours}")

# Create the sql file
sql_file = f"{fcst_dir}/mslp.sql"

try:
   SQLFILE = open(f"{sql_file}\n",'w')
except OSError as error:
    print(f"Got error = {error}")
    sys.exit()

print("delete from official_edits where parameter_code=19;", file = SQLFILE)
for i in range(0,numhours):
   # Construct the valid time
   validstring = validtime.as_text('%Y') + '-' + validtime.as_text('%m') + '-' + validtime.as_text('%d') + ' ' + validtime.as_text('%H:%M:%S')
   #print(f"validstring = {validstring}")
   #print(f"numstations = {numstations}")
   for s in range(0,numstations):
      # Construct the sql statement
      query = f"Insert into official_edits values({id[s]},'{validstring}','{initstring}',{param_code},{pmsl[s]}[{i}],{fcst_source});\n"
      #print(f"query = {query}")
      print(query,file=SQLFILE)

SQLFILE.close()
