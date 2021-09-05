from datetime import date
import os,sys,re,subprocess
from subprocess import PIPE

HOST = 'Mustafas-MacBook-Air.local'
login_user = 'WSI_Data'
login_pass = 'CloudsAndSun!#'

ForecastHour = '12'
params_of = {'15daytcprob_m3': '15daytcprob_m3','bydaytcprob_m3': 'bydaytcprob_m3','bydaytcprob_m1': 'bydaytcprob_m1','15daytcprob_m1': '15daytcprob_m1'}
GFS_prods = {'15daytcprob_m3': '15DAYTC','bydaytcprob_m3': 'BYDAYTC','bydaytcprob_m1': 'BYDAYNCTC','15daytcprob_m1': '15DYNCTC'}

models = ['ECM','GFS']
regions = ['ATL', 'WNP']

today = date.today()
validdate = today.strftime("%Y%m%d")
validdate = validdate.rstrip("\n")

datestr = f"{validdate}{ForecastHour}"
#params = list(params_of.keys())
params = ['bydaytcprob_m3', '15daytcprob_m1', '15daytcprob_m3', 'bydaytcprob_m1']
data_dir = '/data/cfan'
GFS_BASE = '/tmp'
product_dir = f"{GFS_BASE}/text_products"
is_primary = 1

print(f"models = {models}")
print(f"regions = {regions}")
print(f"today = {today}")
print(f"validdate = {validdate}")
print(f"datestr = {datestr}")
print(f"params = {params}")

#------------------------------

for param in params:
    #print(f"param = {param}")
    for model in models:
        #print(f"model = {model}")
        for region in regions:
            #print(f"region = {region}")
            numTries=0
            FileNotFound=''
            #print(f"this is mustafa here {param}")
            default_match = re.search('m3',param)
            #print(f"default_match = {default_match}")
            if (model=='GFS' or default_match) and (region=='WNP'):
                continue

            filename = f"CFAN_{datestr}_{region}_{model}_{param}.nc"
            print(f"filename = {filename}")
            if region == 'WNP':
                filename = filename.replace('_m1','')
                print(f"region equal to WNP and filename = {filename}")

            url = f"https://www.cfanclimate.com/PULL/WSI/{filename}"
            #print(f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{{http_code}}' {url}")
            status_code_obj = subprocess.run(f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{{http_code}}' {url}",stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
            status_code_bi = status_code_obj.stdout
            status_code = status_code_bi.decode("utf-8")
            #print(f"status_code = {status_code}")
            file_found = None

            if status_code == '200':
                file_found = 1
            else:
                file_found = 0

            print("============================")
            print("start section testing Aug-24")
            print(f"file_found = {file_found}")
            print(f"numTries = {numTries}")


            while(file_found == 0 and numTries <= 60):
                print(f"The file {filename} has not yet arrived, sleeping 1 minute",file=sys.stderr)
                os.system('sleep 60')
                print(f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{{http_code}}' {url}")
                status_code_obj = subprocess.run(f"curl -o /dev/null --silent --max-time 3 -u {login_user}:{login_pass} --head --write-out '%{{http_code}}' {url}",stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
                status_code_bi = status_code_obj.stdout
                status_code = status_code_bi.decode("utf-8")

                if status_code == '200':
                    file_found = 1

                numTries += 1
                print(f"numTries = {numTries}")
                if numTries > 60:
                   print(f"The file {filename} has not yet arrived after 60 minutes...moving on",file=sys.stderr)
                   FileNotFound = 'no'

                   try:
                       subprocess.run(f'echo "{filename} missing on {HOST}" | mail -s "CFAN Tropical file has not yet arrived after 60 minutes on {HOST}" rb@atmosphericg2.com',shell=True)
                   except OSError:
                       sys.exit()

                   continue

            if FileNotFound == 'no':
                continue

            print(f"Processing the file {filename}")
            downloaded = 0
            while downloaded == 0:
                print(f"curl -f -o {data_dir}/{filename} -u {login_user}:{login_pass} {url}")
                err = os.system(f"curl -f -o {data_dir}/{filename} -u {login_user}:{login_pass} {url}")
                err = err >> 8
                if err != 0:
                    print(f"error in getting file {err} {url}",file=sys.stderr)
                    os.system('sleep 3')
                else:
                    downloaded = 1


            product = f"{datestr}_{region}_{model}_{params_of[param]}.nc"
            #print(f"product = {product}")

            final = None
            if region == 'WNP':
                final = f"CFANWP{model}{ForecastHour}_{GFS_prods[param]}"
                #print(f"final = {final}")
            else:
                final = f"CFAN{region}{model}{ForecastHour}_{GFS_prods[param]}"
                #print(f"final = {final}")

            print(f"Moving the file {filename} to {product}")
            os.system(f"cp -f {data_dir}/{filename} {data_dir}/{product}")
            #print(f"cp -f {data_dir}/{filename} {data_dir}/{product}")

            print(f"Moving the file {product} to {final}")
            os.system(f"cp -f {data_dir}/{product} {product_dir}/{final}")
            #print(f"cp -f {data_dir}/{product} {product_dir}/{final}")


            if region == 'ATL':
                print(f"Transferring {data_dir}/{product} to energy-research")
                if is_primary == 1:
                    #print(f"scp {data_dir}/{product} op@energy-research1:/archive/real_time/cfan/TCs")
                    os.system(f"scp {data_dir}/{product} op@energy-research1:/archive/real_time/cfan/TCs")


            # Send the File
            print(f"{GFS_BASE}/bin/prod_send.pl -product {final}")
            os.system(f"{GFS_BASE}/bin/prod_send.pl -product {final}")

            # Archive the Product
            print(f"{GFS_BASE}/bin/archive_product {product_dir}/{final}")
            os.system(f"{GFS_BASE}/bin/archive_product {product_dir}/{final}")

if is_primary == 1:
   print("Creating Graphics")

   # Create the Graphics
   print("ssh op@energy-research1 'cd /home/op/ventrice/real_time ; ncl CFAN_TCs.ncl'")
   os.system("ssh op@energy-research1 'cd /home/op/ventrice/real_time ; ncl CFAN_TCs.ncl'")

   # Retrieve the Graphics
   print(f"scp op@energy-research1:/home/op/ventrice/real_time/figures/ECM_Atlantic_\*_{ForecastHour}Z.png {data_dir}")
   os.system(f"scp op@energy-research1:/home/op/ventrice/real_time/figures/ECM_Atlantic_\*_{ForecastHour}Z.png {data_dir}")
   print(f"scp op@energy-research1:/home/op/ventrice/real_time/figures/GEFS_Atlantic_\*_{ForecastHour}Z.png {data_dir}")
   os.system(f"scp op@energy-research1:/home/op/ventrice/real_time/figures/GEFS_Atlantic_\*_{ForecastHour}Z.png {data_dir}")

   # Package and Send the Graphics
   print(f"zip {product_dir}/CALIBTROPFRCST_{ForecastHour} {data_dir}/ECM*png {data_dir}/GEFS*png ; mv {product_dir}/CALIBTROPFRCST_{ForecastHour}.zip {product_dir}/CALIBTROPFRCST_{ForecastHour}")
   os.system(f"zip {product_dir}/CALIBTROPFRCST_{ForecastHour} {data_dir}/ECM*png {data_dir}/GEFS*png ; mv {product_dir}/CALIBTROPFRCST_{ForecastHour}.zip {product_dir}/CALIBTROPFRCST_{ForecastHour}")
   print(f"{GFS_BASE}/bin/prod_send.pl -product CALIBTROPFRCST_{ForecastHour}")
   os.system(f"{GFS_BASE}/bin/prod_send.pl -product CALIBTROPFRCST_{ForecastHour}")

   # Archive the Product
   print(f"{GFS_BASE}/bin/archive_product {product_dir}/CALIBTROPFRCST_{ForecastHour}")
   os.system(f"{GFS_BASE}/bin/archive_product {product_dir}/CALIBTROPFRCST_{ForecastHour}")

   #Clean-up
   print(f"rm {data_dir}/*.png")
   os.system(f"rm {data_dir}/*.png")
