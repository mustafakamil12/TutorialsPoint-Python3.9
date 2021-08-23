from datetime import date
import re,subprocess
from subprocess import PIPE


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

            filename =f"CFAN_{datestr}_{region}_{model}_{param}.nc"
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

            #print(f"file_found = {file_found}")
