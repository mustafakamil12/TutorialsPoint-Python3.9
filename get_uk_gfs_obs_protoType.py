#!/usr/bin/python3 -u

import sys,os,re
import fileinput,subprocess,inspect
#SKIPPED: use Time::Local;
#SKIPPED: use POSIX qw/strftime/;


try:
   OBS=open('/data/gfs/v10/scratch_products/UKGFS_OBS','w')
except OSError:
   sys.exit()

try:
   STATIONS=open('/data/gfs/v10/config/ukgfs.stn','w')
except OSError:
   sys.exit()

stats=STATIONS.readlines().copy
default_var=default_var[0:-1]


end_time=time()
end_str=strftime('%Y-%m-%d %H:%M:00',gmtime(end_time))

start_time=end_time-3600
start_str=strftime('%Y-%m-%d %H:%M:00',gmtime(start_time))

#print "Start time is $start_str\n";
print(file=OBS)

for i in range(0,(len(stats)-1)):
   stat_vals=)

   wsi_code=stat_vals[0]
   icao_code=stat_vals[1]



   #print "Processing $iter_str\n";

   base_command='/usr/local/pgsql/bin/psql -A -t -h gfs-3.twdl.co.uk -F , -d gfsv10 -U gfs -c'
   base_command=base_command + """ \"select valid_time + '5 minutes'::INTERVAL, storage_time + '5 minutes'::INTERVAL, temperature, dew_point, surface_pressure, wind_speed, wind_direction, wind_gusts, visibility, cloud_cover, cloud_height"""
   base_command=base_command + f" from surface_observations where wsi_code = {wsi_code}"
   base_command=base_command + f" AND valid_time >= \'{start_str}\'"
   base_command=base_command + f""" AND valid_time <= \'{end_str}\'\""""
   print(base_command + '')
   try:
      BASE=open(f"{base_command} |",'w')
   except OSError:
      sys.exit()
   base_values=BASE.readline()
   BASE.f.close;

   #        print $base_values;

   default_var=default_var[0:-1]
   base_arr=re.split(',',base_values)
   valid_time=base_arr[0]
   storage_time=base_arr[1]
   temperature=base_arr[2]
   dew_point=base_arr[3]
   pressure=base_arr[4]
   wind_speed=base_arr[5]
   wind_direction=base_arr[6]
   wind_gusts=base_arr[7]
   visibility=base_arr[8]
   cloud_cover=base_arr[9]
   cloud_height=base_arr[10]


   if temperature!='':
      if dew_point=='':
         dew_point='NULL'
      if pressure=='':
         pressure='NULL'
      if wind_speed=='':
         wind_speed='NULL'
      if wind_direction=='':
         wind_direction='NULL'
      if wind_gusts=='':
         wind_gusts='NULL'
      if visibility=='':
         visibility='NULL'
      if cloud_cover=='':
         cloud_cover='NULL'
      if cloud_height=='':
         cloud_height='NULL'

      #            print "info = $cloud_info, height = $cloud_height, cover = $cloud_cover\n";
      print(file=OBS)

print(file=OBS)
OBS.f.close;

os.system('/usr/local/pgsql/bin/psql gfsv10 < /data/gfs/v10/scratch_products/UKGFS_OBS')


