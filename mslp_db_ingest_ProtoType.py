#!/usr/bin/python3 -u

import sys,os,re
import fileinput,subprocess,inspect
#SKIPPED: use FindBin qw($Bin);   # Find directory where this script was executed.
#SKIPPED: use lib "$Bin/../perllib";     # Add library directory to lib path.
#SKIPPED: use strict;
#SKIPPED: use GFS_time;

fcst_file=.pop(0)

bin_dir='/data/gfs/v10/bin'
fcst_dir='/data/gfs/v10/scratch_products'
HOST=os.environ['HOST']

# Time/Date Strings
today=new GFS_time
yyyy=today.as_text('%Y')
mm=today.as_text('%m')
dd=today.as_text('%d')
yyyymmdd=yyyy + mm + dd
inputdate=f"{yyyy}-{mm}-{dd}"

validtime=new GFS_time(f"{inputdate} 00:00:00")
initstring=today.as_text('%Y') + '-' + today.as_text('%m') + '-' + today.as_text('%d') + ' ' + today.as_text('%H:%M:%S')

param_code=19
fcst_source=3

# Check for current forecast file

fcst_file=f"{fcst_dir}/mslp.txt"
print()
while not os.path.exists(f"{fcst_file}") and ():
   print()
   sleep 60
if  not os.path.exists(fcst_file):
   try:
      MAILMSG=open(f'| mail -s \"Problem with MSLP forecast ingest on {HOST}\" energyformatters\@wsi.com','w')
   except OSError:
      sys.exit()
   print(file=MAILMSG)
   MAILMSG.f.close;
   sys.exit(f"{fcst_file} missing on {HOST}, exiting\n")

# Read the forecast file
numstations=0
hournum=0
id=None
data=None
pmsl=None
s=0
i=0
try:
   FCSTFILE=open(f"{fcst_file}",'r')
except OSError:
   sys.exit()
while FCSTFILE.readline():
   data=re.split
   i=0
   id[s]=data.pop(0)
   for d(data
      pmsl[s][i]=d
      i+=1
   s+=1
numstations=s-1
numhours=i
FCSTFILE.f.close;

# Create the sql file
sql_file=f"{fcst_dir}/mslp.sql"
try:
   SQLFILE=open(f"{sql_file}\n",'w')
except OSError:
   sys.exit()
printf(file=SQLFILE)
for i in range(0,numhours):
   # Construct the valid time
   validstring=validtime.as_text('%Y') + '-' + validtime.as_text('%m') + '-' + validtime.as_text('%d') + ' ' + validtime.as_text('%H:%M:%S')
   for s in range(0,numstations):
      # Construct the sql statement
      query=f"Insert into official_edits values({id[s]},'{validstring}','{initstring}',{param_code},{pmsl[s]}[{i}],{fcst_source});\n"
      printf(file=SQLFILE)
SQLFILE.f.close;

# Run ingest queries
cmd=f"psql -q -f {sql_file}"
if os.system(cmd)!=0:
   try:
      MAIL=open(f'| mail -s \"Problem with MSLP forecast ingest on {HOST}\" energyformatters\@wsi.com','w')
   except OSError:
      sys.exit()
   print(file=MAIL)
   MAIL.f.close;
   print()
else:
   print()
