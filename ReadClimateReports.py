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
print("subprocess_rc = ", subprocess_rc)
HOSTNAME_bi = HOSTNAME_bi.stdout
HOSTNAME = HOSTNAME_bi.decode("utf-8")
print(f"HOSTNAME = {HOSTNAME}")
HOSTNAME = HOSTNAME[0:-1]
print(f"HOSTNAME = {HOSTNAME}")

# The final output file containing the Max/Min values
# derived from the Climate Reports
print(f"{dir}/scratch_products/ClimateReportMaxMins.sql")
sql_file = f"{dir}/scratch_products/ClimateReportMaxMins.sql"

try:
    OUTPUT = open(f"{sql_file}",'r')
except OSError:
    print(f"Error occurred to open {sql_file} ...")
    sys.exit()

# Open the Climate Bulleting Config File for reading
print(f"{dir}/config/ClimateBulletinSites.cfg")
STN_Lines = []
try:
    with open (f"{dir}/config/ClimateBulletinSites.cfg", "r") as STN_File:
        STN_Lines_raw = STN_File.readlines()
        for line in STN_Lines_raw:
            STN_Lines.append(line.rstrip("\n"))
except OSError:
    print(f"Can't Open Station File: {dir}/config/limateBulletinSites.cfg")
    sys.exit()

print(f"STN_Lines = {STN_Lines}")

# Determine yesterdays day
today = date.today()
currentDate = today.strftime("%Y-%m-%d")
todaysyear = today.strftime("%Y")
todaysmon = today.strftime("%m")
todaysday = today.strftime("%d")

print(f"todaysyear = {todaysyear}")
print(f"todaysmon = {todaysmon}")
print(f"todaysday = {todaysday}")
print(f"timedelta(days=-1) = {timedelta(days=-1)}")
#modifiedDate = currentDate + datetime.timedelta(days=-1)
#print(f"modifiedDate = {modifiedDate}")
#[year,month,yesterday] = Add_Delta_Days (todaysyear,todaysmon,todaysday,-1)
