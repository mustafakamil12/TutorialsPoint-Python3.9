import re

config_options = "-gfs -3"
post_proc_file = " 11 .11 | 22 .22 | 33 .33"

default_match = re.match(r'-reltime +(-?[0-9]+)',config_options)
default_match1 = re.match(r'-gfs(.+)$',config_options)

if default_match:
    print(default_match.group(0))
if default_match1:
    print(default_match1.group(0))

if len(post_proc_file) > 0:
  post_proc_scripts = re.split(r' *\| *',post_proc_file)
  print("post_proc_scripts: ", post_proc_scripts)
  pp = None
  for pp in post_proc_scripts:
     default_match = re.match('([^ ]*) (.*)',pp)
     if (default_match.group(0)):
        pp_com = default_match.group(1)
        pp_param = default_match.group(2)
     else:
        pp_com = pp
        pp_param = ''

print(pp_com)
print(pp_param)
print(default_match)
