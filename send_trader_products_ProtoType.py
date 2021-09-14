#!/usr/bin/python3 -u

import sys,os,re
import fileinput,subprocess,inspect
base_path=os.environ['GFS_BASE']
is_primary=subprocess.run('/home/gfs/bin/gfs_primary',capture_output=True,text=True,shell=True)
subprocess_rc=is_primary.returncode
is_primary=is_primary.stdout


remote_imageDir='/usr/local/apache/htdocs/forecasts/weather/realtime'
webserver='energy-web'
products={'WEFFECTS_FIVDAY_FL_CONUS.gif','TRADER_1-5DAY','WEFFECTS_6TO10_FL_AVG6TO10.gif','TRADER_6-10DAY','WEFFECTS_11TO15_FL_CONUS.gif','TRADER_11-15DAY'}

for image(sort.keys products
   cur_time=time
   logs([f"Checking the file {image} on {webserver}"])
   update_time=subprocess.run(f"sshto -l op {webserver} GetDateModifiedInEpoch {remote_imageDir}/{image}",capture_output=True,text=True,shell=True)
   subprocess_rc=update_time.returncode
   update_time=update_time.stdout
   timeDiff='%d' % ( (cur_time-update_time))

   # Check to ensure image has been created in the past minute
   if timeDiff<60:
      #Remove any previous image since the wget will not overwrite 
      os.system(f"rm {base_path}/text_products/{products[image]}")
      os.system(f'wget -q -T 180 -c -O  {base_path}/text_products/{products[image]} \"ftp://op:doctor\@energy-web/{remote_imageDir}/{image}\"')

      if is_primary==0:
         logs(['Not on LIVE system. Not sending'])
      else:
         os.system(f"/data/gfs/v10/bin/prod_send.pl -product {products[image]}")
         logs([f"The image {image} has been transferred"])

def logs(perl_arg_array):
   msg=.pop(0)

   currentTime=subprocess.run('date +%y%m%d:%H%m%Z',capture_output=True,text=True,shell=True)
   subprocess_rc=currentTime.returncode
   currentTime=currentTime.stdout
   currentTime=currentTime.rstrip("\n")

   print()

