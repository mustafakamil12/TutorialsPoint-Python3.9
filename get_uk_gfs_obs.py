#!/usr/bin/python3
import sys,os,re
import fileinput,subprocess,inspect,time,datetime

try:
   OBS = open('/data/gfs/v10/scratch_products/UKGFS_OBS','w')
except OSError:
   #print(f"UKGFS_OBS is not found in /data/gfs/v10/scratch_products/")
   sys.exit()
try:
   STATIONS = open('/data/gfs/v10/config/ukgfs.stn','r')
except OSError:
   #print(f"ukgfs.stn is not found in /data/gfs/v10/config/")
   sys.exit()

#print(f"OBS = {OBS} and STATIONS = {STATIONS}")
stats = STATIONS.read().splitlines()
#print(f"stats = {stats}")

end_time = time.time()
end_str = time.strftime('%Y-%m-%d %H:%M:00',time.gmtime(end_time))

start_time = end_time - 3600
start_str = time.strftime('%Y-%m-%d %H:%M:00',time.gmtime(start_time))

#print(f"end_str = {end_str} and start_str = {start_str}")

print("BEGIN TRANSACTION;",file=OBS)
#print(f"stats = {stats}")
for i in range(0,len(stats)):
    stat_vals = stats[i].split(',')
    #print(f"stat_vals = {stat_vals}")
    wsi_code = stat_vals[0]
    icao_code = stat_vals[1]
    #print(f"wsi_code = {wsi_code}")
    #print(f"icao_code = {icao_code}")
    #base_command = '/usr/local/pgsql/bin/psql -A -t -h gfs-3.twdl.co.uk -F , -d gfsv10 -U gfs -c'
    base_command = '/usr/bin/psql -A -t -h gfs-3.twdl.co.uk -F , -d gfsv10 -U gfs -c'
    base_command = base_command + """ \"select valid_time + '5 minutes'::INTERVAL, storage_time + '5 minutes'::INTERVAL, temperature, dew_point, surface_pressure, wind_speed, wind_direction, wind_gusts, visibility, cloud_cover, cloud_height"""
    base_command = base_command + f" from surface_observations where wsi_code = {wsi_code}"
    base_command = base_command + f" AND valid_time >= \'{start_str}\'"
    base_command = base_command + f""" AND valid_time <= \'{end_str}\'\""""
    print(base_command + '')
    