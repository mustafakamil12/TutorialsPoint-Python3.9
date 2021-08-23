from datetime import date
import re

ForecastHour = '12'
params_of = {'15daytcprob_m3': '15daytcprob_m3','bydaytcprob_m3': 'bydaytcprob_m3','bydaytcprob_m1': 'bydaytcprob_m1','15daytcprob_m1': '15daytcprob_m1'}
GFS_prods = {'15daytcprob_m3': '15DAYTC','bydaytcprob_m3': 'BYDAYTC','bydaytcprob_m1': 'BYDAYNCTC','15daytcprob_m1': '15DYNCTC'}

models = ['ECM','GFS']
regions = ['ATL', 'WNP']

today = date.today()
validdate = today.strftime("%Y%m%d")
validdate = validdate.rstrip("\n")

datestr = f"{validdate}{ForecastHour}"
params = list(params_of.keys())

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
            default_match = re.match('m3',param)
            if (model=='GFS' or default_match) and (region=='WNP'):
                continue



            filename =f"CFAN_{datestr}_{region}_{model}_{param}.nc"
            print(f"filename = {filename}")
            if region == 'WNP':
                filename = filename.replace('_m1','')
                print(f"region equal to WNP and filename = {filename}")
