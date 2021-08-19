import sys,os
# Read the forecast file
fcst_dir = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Perl'
fcst_file = f"{fcst_dir}/mslp.txt"


numstations = 0
hournum = 0
id = []
data = []
pmslRow = []
pmsl = []
s = 0
i = 0

try:
   FCSTFILE = open(f"{fcst_file}",'r')
except OSError as error:
    print(f"Got error = {error}")
    sys.exit()

FCSTFILE_lines = FCSTFILE.readlines()
print(f"FCSTFILE_lines = {FCSTFILE_lines}")
#print(len(FCSTFILE_lines))
#print(f"FCSTFILE_lines[0] = {FCSTFILE_lines[0]}")
print(f"length of FCSTFILE_lines = {FCSTFILE_lines}")
while FCSTFILE_lines:
    data = FCSTFILE_lines[0].split(' ')
    print(f"data = {data}")
    i = 0
    id.insert(s,data.pop(0))
    pmsl.insert(s,data)
    FCSTFILE_lines.pop(0)
    s += 1
print(f"pmsl = {pmsl}")
