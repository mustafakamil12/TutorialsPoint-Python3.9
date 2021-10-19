import re
newLine = "30 20,21 * * *   /pgs/bin/TimeZoneHour US/Eastern 16 && /pgs/bin/run_pgs_script product_build_send -cycle 'Afternoon'"
newLine1 = "00 3,4 * * *    /pgs/bin/TimeZoneHour US/Eastern 23 && /pgs/bin/run_pgs_script product_build_send -cycle ET_11PM > /dev/null 2>&1"

cycle = re.findall(r'cycle .\S+',newLine1)
print(cycle)
