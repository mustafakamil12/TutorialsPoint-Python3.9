#!/usr/bin/python3 -u

import sys,os,re
import fileinput,subprocess,inspect
#SKIPPED: use strict;
#SKIPPED: use warnings;

#SKIPPED: use FindBin qw($Bin);   # Find directory where this script was executed.
#SKIPPED: use lib "$Bin/../perllib";     # Add library directory to lib path.

ForecastHour=.pop(0)

#Setup Config
HOST=os.environ['HOST']
GFS_BASE=os.environ['GFS_BASE']
product_dir=f"{[GFS_BASE]}/text_products"
data_dir='/data/cfan'
login_user='WSI_Data'
login_pass='CloudsAndSun!#'
is_primary='/home/gfs/bin/gfs_primary'
params_of=('15daytcprob_m3': '15daytcprob_m3','bydaytcprob_m3': 'bydaytcprob_m3','bydaytcprob_m1': 'bydaytcprob_m1','15daytcprob_m1': '15daytcprob_m1',)

GFS_prods=('15daytcprob_m3': '15DAYTC','bydaytcprob_m3': 'BYDAYTC','bydaytcprob_m1': 'BYDAYNCTC','15daytcprob_m1': '15DYNCTC',)

models=qw(ECM GFS)
regions=qw(ATL WNP)

validdate='date +%Y%m%d'
validdate=validdate.rstrip("\n")

datestr=f"{[validdate]}{[ForecastHour]}"
params=params_of.keys

for param(params
   for model(models
      for region(regions
         numTries=0
         FileNotFound=''

         if (model=='GFS' or re.match('m3',param)) and (region=='WNP'):
            continue 

         filename=f"CFAN_{[datestr]}_{[region]}_{[model]}_{[param]}.nc"
         if region=='WNP':
            filename=str.replace('_m1','_m1',1)filename)

         url=f"https://www.cfanclimate.com/PULL/WSI/{filename}"
         status_code=f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{http_code}' {url}"
         file_found=None

         if status_code=='200':
            file_found=1
         else:
            file_found=0

         while file_found==0 and numTries<=60:

            print(file=sys.stderr)
            sleep 60
            status_code=subprocess.run(f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{http_code}' {url}",capture_output=True,text=True,shell=True)
            subprocess_rc=status_code.returncode
            status_code=status_code.stdout

            if status_code=='200':
               file_found=1

            numTries+=1

            if numTries>60:
               print(file=sys.stderr)
               FileNotFound='no'

               try:
                  MAILMSG=open(f'| mail -s \"CFAN Tropical file has not yet arrived after 60 minutes on {HOST}\" rb\@atmosphericg2.com','w')
               except OSError:
                  sys.exit()
               print(file=MAILMSG)
               MAILMSG.f.close;

               continue 

         if FileNotFound=='no':
            continue 

         print()
         downloaded=0
         while downloaded==0:
            err=os.system(f"curl -f -o {[data_dir]}/{[filename]} -u {[login_user]}:{[login_pass]} {url}")
            err=err>>8
            if err!=0:
               print(file=sys.stderr)
               sleep([3])
            else:
               downloaded=1

         product=f"{[datestr]}_{[region]}_{[model]}_{[params_of[param]}}.nc"

         final=None
         if region=='WNP':
            final=f"CFANWP{[model]}{[ForecastHour]}_{[GFS_prods[param]}}"
         else:
            final=f"CFAN{[region]}{[model]}{[ForecastHour]}_{[GFS_prods[param]}}"

         print()
         os.system(f"cp -f {data_dir}/{filename} {data_dir}/{product}")

         print()
         os.system(f"cp -f {data_dir}/{product} {product_dir}/{final}")


         if region=='ATL':
            print()
            if is_primary==1:
               os.system(f"scp {data_dir}/{product} op\@energy-research1:/archive/real_time/cfan/TCs")

         # Send the File
         os.system(f"{GFS_BASE}/bin/prod_send.pl -product {final}")

         # Archive the Product
         os.system(f"{GFS_BASE}/bin/archive_product {product_dir}/{final}")

if is_primary==1:
   print()

   # Create the Graphics
   os.system("ssh op\@energy-research1 'cd /home/op/ventrice/real_time ; ncl CFAN_TCs.ncl'")

   # Retrieve the Graphics
   os.system(f"scp op\@energy-research1:/home/op/ventrice/real_time/figures/ECM_Atlantic_\*_{[ForecastHour]}Z.png {data_dir}")
   os.system(f"scp op\@energy-research1:/home/op/ventrice/real_time/figures/GEFS_Atlantic_\*_{[ForecastHour]}Z.png {data_dir}")

   # Package and Send the Graphics
   os.system(f"zip {product_dir}/CALIBTROPFRCST_{[ForecastHour]} {data_dir}/ECM*png {data_dir}/GEFS*png ; mv {product_dir}/CALIBTROPFRCST_{[ForecastHour]}.zip {product_dir}/CALIBTROPFRCST_{[ForecastHour]}")
   os.system(f"{GFS_BASE}/bin/prod_send.pl -product CALIBTROPFRCST_{[ForecastHour]}")

   # Archive the Product
   os.system(f"{GFS_BASE}/bin/archive_product {product_dir}/CALIBTROPFRCST_{[ForecastHour]}")

   #Clean-up
   os.system(f"rm {data_dir}/*.png")
