import re,os
prod_id = 'BOFAHRLYFCST12AM'
error_count = 0
format_cmdline = ''

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

print(f"pp_com = {pp_com}")
print(f"pp_param = {pp_param}")
print(default_match)

base_path = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
post_proc_dir = f"{base_path}/formatter_post_proc"
post_proc_path = f"{post_proc_dir}/{pp_com}"
# check for presents and executability of post_proc file.
# os.access(post_proc_path, os.X_OK)


if not os.access(post_proc_path, os.X_OK):
    print(f"Formatter Error, could not build {prod_id}, missing post-proc file: {post_proc_path}")
    error_count += 1

format_cmdline += f" | {post_proc_path} {pp_param} "
print("format_cmdline: ", format_cmdline)
