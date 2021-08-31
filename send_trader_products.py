#!/usr/bin/python3 -u

import sys,os,re,time,datetime
import fileinput,subprocess,inspect
from os import environ
from subprocess import PIPE
from datetime import date
from datetime import datetime

#base_path = os.environ['GFS_BASE']
base_path = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
#is_primary_bi = subprocess.run("/home/gfs/bin/gfs_primary",stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
#subprocess_rc = is_primary_bi.returncode
#print("subprocess_rc = ", subprocess_rc)
#is_primary_bi = is_primary_bi.stdout
#is_primary = int(is_primary_bi.decode("utf-8"))

is_primary = 1

remote_imageDir = '/usr/local/apache/htdocs/forecasts/weather/realtime'
webserver = 'energy-web'
products = {'WEFFECTS_FIVDAY_FL_CONUS.gif':'TRADER_1-5DAY','WEFFECTS_6TO10_FL_AVG6TO10.gif':'TRADER_6-10DAY','WEFFECTS_11TO15_FL_CONUS.gif':'TRADER_11-15DAY'}

#--------------------------------------------
def logs(msg):
    currentTime_bi = subprocess.run('date +%y%m%d:%H%m%Z',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
    currentTime_rc = currentTime_bi.returncode
    currentTime_bi = currentTime_bi.stdout
    currentTime = currentTime_bi.decode("utf-8")
    currentTime = currentTime.rstrip("\n")
    #print(f"currentTime = {currentTime}")

    print(f"{currentTime}: {msg}")


for image in products:
    #print(f"image = {image}")
    cur_time = int(time.time())
    logs(f"Checking the file {image} on {webserver}")

    print(f"sshto -l op {webserver} GetDateModifiedInEpoch {remote_imageDir}/{image}")
    update_time_bi = subprocess.run(f"sshto -l op {webserver} GetDateModifiedInEpoch {remote_imageDir}/{image}",capture_output=True,text=True,shell=True)
    update_time_rc = update_time_bi.returncode
    update_time_bi = update_time_bi.stdout
    update_time = update_time_bi
    #update_time = update_time_bi.decode("utf-8")

    update_time = cur_time + (24*60*60) #For testing purposes
    timeDiff = cur_time - update_time
    timeDiff = int(timeDiff / (24*60*60))
    print(f"timeDiff = {timeDiff}")

       # Check to ensure image has been created in the past minute
    if timeDiff < 60:
        #Remove any previous image since the wget will not overwrite
        os.system(f"rm {base_path}/text_products/{products[image]}")
        os.system(f'wget -q -T 180 -c -O  {base_path}/text_products/{products[image]} \"ftp://op:doctor@energy-web/{remote_imageDir}/{image}\"')

        if is_primary == 0:
            logs('Not on LIVE system. Not sending')
        else:
            os.system(f"/data/gfs/v10/bin/prod_send.pl -product {products[image]}")
            logs(f"The image {image} has been transferred")
