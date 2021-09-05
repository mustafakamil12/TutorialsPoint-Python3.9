#!/usr/bin/python3 -u

import sys,os,re
import fileinput,subprocess,inspect
#SKIPPED: use strict;

# Load Date:Calc function
#SKIPPED: use Date::Calc qw(Add_Delta_Days);

max=None
min=None
state=None
dir=os.environ['GFS_BASE']
skybaseuser='atmospheric_g2'
skybasehost='arc-stgsky-agg'
HOSTNAME='/bin/hostname'
HOSTNAME=HOSTNAME[0:-1]

# The final output file containing the Max/Min values
# derived from the Climate Reports
sql_file=f"{dir}/scratch_products/ClimateReportMaxMins.sql"
try:
   OUTPUT=open(f"{sql_file}",'w')
except OSError:
   sys.exit()

# Open the Climate Bulleting Config File for reading
if(STN:=open(f"{dir}/config/ClimateBulletinSites.cfg",'w')):
   sys.exit(f"Can't Open Station File: {dir}/config/limateBulletinSites.cfg")
Stns=STN.readline()

# Determine yesterdays day
todaysyear='date +%Y'
todaysmon='date +%m'
todaysday='date +%d'
[year,month,yesterday]=Add_Delta_Days(todaysyear,todaysmon,todaysday,-1)
if month<10:
   month=f"0{month}"

if yesterday<10:
   yesterday=f"0{yesterday}"

valid_date=f"{[year]}-{[month]}-{[yesterday]}"
todays_date='date +%Y-%m-%d'
todays_date=todays_date.rstrip("\n")
stn=mintemp=maxtemp=None

for stn(Stns
   stn=stn.rstrip("\n")

   base_command=f"""/usr/local/pgsql/bin/psql -A -t -h {skybasehost} -d skybase -U {skybaseuser} -c \"select min_temperature,max_temperature from atmospheric_g2.nws_cli_data(now(), '{valid_date}') where faa_site_id ='{stn}' and report_type='M';\""""

   try:
      BASE=open(f"{base_command} |",'w')
   except OSError:
      sys.exit()
   Temps=BASE.readline()
   Temps=Temps.rstrip("\n")
   BASE.f.close;

   if Temps!='':
      [mintemp,maxtemp]=re.split('\|',Temps)

      mintemp=(mintemp-32)*(5/9)
      maxtemp=(maxtemp-32)*(5/9)

      printf(f"update max_temperature_observations set max_temperature=%.2f where valid_date='{todays_date}' and wsi_code in (select wsi_code from full_station_list where icao_code='K{stn}');\n",maxtemp,file=OUTPUT)

      printf(f"insert into max_temperature_observations (wsi_code,valid_date,valid_time,max_temperature) select (select wsi_code from full_station_list where icao_code='K{stn}'),'{todays_date}','{todays_date} 13:30:00+00',%.2f where not exists (select 1 from max_temperature_observations where valid_date='{todays_date}' and wsi_code in (select wsi_code from full_station_list where icao_code='K{stn}'));\n",maxtemp,file=OUTPUT)

      printf(f"update min_temperature_observations set min_temperature=%.2f where valid_date='{todays_date}' and wsi_code in (select wsi_code from full_station_list where icao_code='K{stn}');\n",mintemp,file=OUTPUT)

      printf(f"insert into min_temperature_observations (wsi_code,valid_date,valid_time,min_temperature) select (select wsi_code from full_station_list where icao_code='K{stn}'),'{todays_date}','{todays_date} 13:30:00+00',%.2f where not exists (select 1 from min_temperature_observations where valid_date='{todays_date}' and wsi_code in (select wsi_code from full_station_list where icao_code='K{stn}'));\n",mintemp,file=OUTPUT)


# Run ingest queries
cmd=f"/usr/local/pgsql/bin/psql -q -f {sql_file}"
if os.system(cmd)!=0:
   try:
      MAIL=open(f'| mail -s \"Problem with Climate Report Ingest on {HOSTNAME}\" rb\@atmosphericg2.com','w')
   except OSError:
      sys.exit()
   print(file=MAIL)
   MAIL.f.close;
   print()
else:
   print()
