import sys
#sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")
import re,GFS_time,GFS_timezone
from GFS_time import *
from GFS_timezone import *

address = "#TZ=godric#"
address = "godric.phoenix@gmail.com"

default_match = re.match('#TZ=(\w*)#',address)

print(f"default_match = {default_match}")
print(f"default_match = {default_match.group(0)}")
print(f"default_match = {default_match.group(1)}")

current_time = GFS_time([])
print(f"current_time = {current_time}")
print(f"type of current_time = {type(current_time.get_time_t())}")
offset = 0

if (default_match):

    offset = GFS_timezone.get_timezone_offset([current_time.get_time_t(),default_match.group(1)])
    print(f"offset = {offset}")
    address = re.sub('#TZ=(\w*)#',"", address)
final_address = current_time.as_text(address,offset)
print(f"final_address = {final_address}")

final_address = re.sub('\$','\\\$',final_address)
final_address = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{default_match.group(1)}\"\'\"\'\"\'" ,final_address)

print(f"after all --> final_address = {final_address}")
