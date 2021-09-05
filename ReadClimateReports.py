#!/usr/bin/python3 -u

import sys,os,re,time,datetime
import fileinput,subprocess,inspect
from os import environ
from subprocess import PIPE
from datetime import date

max = None
min = None
state = None
#dir = os.environ['GFS_BASE']
dir = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
skybaseuser = 'atmospheric_g2'
skybasehost = 'arc-stgsky-agg'
HOSTNAME = '/bin/hostname'


HOSTNAME_bi = subprocess.run("/bin/hostname",stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
subprocess_rc = HOSTNAME_bi.returncode
#print("subprocess_rc = ", subprocess_rc)
HOSTNAME_bi = HOSTNAME_bi.stdout
HOSTNAME = HOSTNAME_bi.decode("utf-8")
#print(f"HOSTNAME = {HOSTNAME}")
HOSTNAME = HOSTNAME[0:-1]
#print(f"HOSTNAME = {HOSTNAME}")

# The final output file containing the Max/Min values
# derived from the Climate Reports
#print(f"{dir}/scratch_products/ClimateReportMaxMins.sql")
sql_file = f"{dir}/scratch_products/ClimateReportMaxMins.sql"

try:
    OUTPUT = open(f"{sql_file}",'r')
except OSError:
    print(f"Error occurred to open {sql_file} ...")
    sys.exit()

# Open the Climate Bulleting Config File for reading
#print(f"{dir}/config/ClimateBulletinSites.cfg")
STN_Lines = []
try:
    with open (f"{dir}/config/ClimateBulletinSites.cfg", "r") as STN_File:
        STN_Lines_raw = STN_File.readlines()
        for line in STN_Lines_raw:
            STN_Lines.append(line.rstrip("\n"))
            Stns = STN_Lines
except OSError:
    print(f"Can't Open Station File: {dir}/config/limateBulletinSites.cfg")
    sys.exit()

#print(f"STN_Lines = {STN_Lines}")

# Determine yesterdays day
today = date.today()
currentDate = today.strftime("%Y-%m-%d")
todaysyear = today.strftime("%Y")
todaysmon = today.strftime("%m")
todaysday = today.strftime("%d")
modifiedDate = datetime.datetime.strptime(currentDate, "%Y-%m-%d") + datetime.timedelta(days=-1)

#print(f"todaysyear = {todaysyear}")
#print(f"todaysmon = {todaysmon}")
#print(f"todaysday = {todaysday}")
#print(f"datetime.timedelta(days=-1) = {datetime.timedelta(days=-1)}")
#print(f"modifiedDate = {modifiedDate}")

year = int(modifiedDate.strftime("%Y"))
month = int(modifiedDate.strftime("%m"))
yesterday = int(modifiedDate.strftime("%d"))

#print("Before")
#print(f"year = {year}")
#print(f"month = {month}")
#print(f"yesterday = {yesterday}")

if month < 10:
    month = f"0{month}"

if yesterday < 10:
   yesterday = f"0{yesterday}"

#print("After")
#print(f"year = {year}")
#print(f"month = {month}")
#print(f"yesterday = {yesterday}")

valid_date = f"{year}-{month}-{yesterday}"
todays_date = today.strftime("%Y-%m-%d")
todays_date = todays_date.rstrip("\n")
#print(f"todays_date = {todays_date}")
stn = mintemp = maxtemp = None

for stn in Stns:
    stn = stn.rstrip("\n")
    #print(f"stn = {stn}")
    #print(f"""/usr/local/pgsql/bin/psql -A -t -h {skybasehost} -d skybase -U {skybaseuser} -c \"select min_temperature,max_temperature from atmospheric_g2.nws_cli_data(now(), '{valid_date}') where faa_site_id ='{stn}' and report_type='M';\"""")
    #base_command = f"""/usr/local/pgsql/bin/psql -A -t -h {skybasehost} -d skybase -U {skybaseuser} -c \"select min_temperature,max_temperature from atmospheric_g2.nws_cli_data(now(), '{valid_date}') where faa_site_id ='{stn}' and report_type='M';\""""
    print(f"""/usr/bin/psql -A -t -h {skybasehost} -d skybase -U {skybaseuser} -c \"select min_temperature,max_temperature from atmospheric_g2.nws_cli_data(now(), '{valid_date}') where faa_site_id ='{stn}' and report_type='M';\"""")
    base_command = f"""/usr/bin/psql -A -t -h {skybasehost} -d skybase -U {skybaseuser} -c \"select min_temperature,max_temperature from atmospheric_g2.nws_cli_data(now(), '{valid_date}') where faa_site_id ='{stn}' and report_type='M';\""""

    try:
        BASE_bi = subprocess.run(base_command,stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        BASE_rc = BASE_bi.returncode
        BASE_bi = BASE_bi.stdout
        BASE = BASE_bi.decode("utf-8")
        BASE = BASE.rstrip("\n")
        Temps= BASE
    except OSError:
        sys.exit()

    if Temps != "":
        [mintemp,maxtemp] = re.split('\|',Temps)

        mintemp = (mintemp - 32) * (5/9)
        maxtemp = (maxtemp - 32) * (5/9)

# Run ingest queries
#cmd = f"/usr/local/pgsql/bin/psql -q -f {sql_file}"
cmd = f"/usr/bin/psql -q -f {sql_file}"
if os.system(cmd)!= 0:
    try:
        subprocess.run(f'echo "Problem with Climate Report Ingest on {HOSTNAME}" | mail -s "psql failed while ingesting {sql_file} on {HOSTNAME}" rb@atmosphericg2.com',shell=True)
        print(f"Ingest of {sql_file} into max/min observation tables failed")
    except OSError:
        sys.exit()

else:
    print(f"{sql_file} successfully ingested into max/min observation tables")
