from datetime import date
import os,sys,re,subprocess
from subprocess import PIPE

HOST = 'Mustafas-MacBook-Air.local'
GFS_BASE = '/data/gfs/v10'
product_dir = "/data/gfs/v10/text_products"
data_dir = "/data/cfan"
login_user = 'WSI_Data'
login_pass = 'CloudsAndSun!#'

ForecastHour = '12'
params_of = {'15daytcprob_m3': '15daytcprob_m3','bydaytcprob_m3': 'bydaytcprob_m3','bydaytcprob_m1': 'bydaytcprob_m1','15daytcprob_m1': '15daytcprob_m1'}
GFS_prods = {'15daytcprob_m3': '15DAYTC','bydaytcprob_m3': 'BYDAYTC','bydaytcprob_m1': 'BYDAYNCTC','15daytcprob_m1': '15DYNCTC'}

models = ['ECM','GFS']
regions = ['ATL', 'WNP']
region = 'ATL'
model = 'GFS'

today = date.today()
validdate = today.strftime("%Y%m%d")
validdate = validdate.rstrip("\n")

datestr = f"{validdate}{ForecastHour}"
#params = list(params_of.keys())
params = ['bydaytcprob_m3', '15daytcprob_m1', '15daytcprob_m3', 'bydaytcprob_m1']
param = 'bydaytcprob_m3'
url = "https://www.cfanclimate.com/PULL/WSI/CFAN_2021082512_ATL_ECM_15daytcprob_m3.nc"

filename = f"CFAN_{datestr}_{region}_{model}_{param}.nc"

downloaded = 0
while downloaded == 0:
    print(f"curl -f -o {data_dir}/{filename} -u {login_user}:{login_pass} {url}")
    err = os.system(f"curl -f -o {data_dir}/{filename} -u {login_user}:{login_pass} {url}")
    print(f"err = {err}")
    err = err >> 8
    print(f"err after shift to 8 = {err}")
    if err != 0:
        print(f"error in getting file {err} {url}",file=sys.stderr)
        os.system('sleep 3')
    else:
        downloaded = 1
