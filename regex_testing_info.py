import re

config_options = "-gfs -3"

default_match = re.match(r'-reltime +(-?[0-9]+)',config_options)

default_match1 = re.match(r'-gfs(.+)$',config_options)

if default_match:
    print(default_match.group(0))
if default_match1:
    print(default_match1.group(0))
