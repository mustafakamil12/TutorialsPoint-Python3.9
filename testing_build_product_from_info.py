from GFS_time import *

bpfiArr =  ['BOFAHRLYFCST12AM', 'frmt_bofa_hourly_fcst', 'bofa_stn', '', '']
global_format_obj = GFS_time([])
global_format_time = global_format_obj.get_time_t()
build_count = 0
base_path = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
output_dir = f"{base_path}/text_products"
formatter_dir = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/format_files_pl" # /data/gfs/v10/format_files
formatter_pl_dir = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/format_files_pl" # /pgs/format_files_pl
error_count = 0
warning_count = 0
extra_args = ''
post_proc_dir = f"{base_path}/formatter_post_proc"
aborts_disabled = 0
pending_abort = 0
old_output_dir = f"{base_path}/old_text_products"

#--------------------------------------------------------------------------------------------------
def file_age(file_age_array):
   print("----file_age----")
   print("file_age_array: ", file_age_array)
   age = 0
   fname = file_age_array.pop(0)
   print("fname: ", fname)
   print("os.path.isfile(fname) = ", os.path.isfile(fname))
   if os.path.isfile(fname):
      fstat = os.stat(fname)
      print("fstat: ", fstat)
      if (len(fstat)) < 9:
         return('NO FILE')
      age = int(time.time()) - fstat[9]
      print("age: ", age)
   else:
      return('NO FILE')
   return age

def report_error(errMsg):
   print("----report_error----")
   print(errMsg ,file=sys.stderr)
   #GFS_syslog.frmt_log_error(errMsg)
def disable_abort():
   global aborts_disabled
   print("----disable_abort----")
   aborts_disabled = 1

def enable_abort():
   print("----enable_abort----")
   global pending_abort,aborts_disabled
   aborts_disabled = 0
   if pending_abort:
      abort_handler('ABRT')

def issue_product_build(ipbArray):
   global error_count
   print("-----issue_product_build-----")
   prod_id = ipbArray.pop(0)
   cmd = ipbArray.pop(0)

   start_time = time.time()

   GFS_syslog.frmt_log_info(f"Begin product build for {prod_id}")
   GFS_syslog.frmt_log_info(f"Command for {prod_id} is {cmd}")

   build_start = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time()))
   #print(f"""psql -c \"update product_generation_log set build_start = \'{build_start}\' where product_name = \'{prod_id}\';\"""")
   #os.system(f"""psql -c \"update product_generation_log set build_start = \'{build_start}\' where product_name = \'{prod_id}\';\"""")

   print(f"""psql -h skybase-2-dev.cv9bnu4vuygm.us-east-1.rds.amazonaws.com gfsv10 postgres -c \"update product_generation_log set build_start = \'{build_start}\' where product_name = \'{prod_id}\';\"""")
   os.system(f"""psql -h skybase-2-dev.cv9bnu4vuygm.us-east-1.rds.amazonaws.com gfsv10 postgres -c \"update product_generation_log set build_start = \'{build_start}\' where product_name = \'{prod_id}\';\"""")

   ret_stat = os.system(cmd)
   print("ret_stat: ", ret_stat)
   end_time = time.time()

   min = int((end_time - start_time)/60)
   sec = (end_time - start_time) - min*60
   elapsed = "%02d:%02d" % (min,sec)

   if ret_stat != 0:
      report_error(f"Fatal error running formatter for {prod_id}")
      GFS_syslog.frmt_log_error(f"Completed product build for {prod_id} with fatal error, {elapsed}")
      error_count += 1
      GFS_syslog.frmt_log_info(f"Completed product build for {prod_id} with fatal error, {elapsed}")
      print(f"Completed product build for {prod_id}, {elapsed} with fatal error")
   else:
      GFS_syslog.frmt_log_info(f"Completed product build for {prod_id}, {elapsed}")
      print(f"Completed product build for {prod_id}, {elapsed}")

#--------------------------------------------------------------------------------------------------

def build_product_from_info(bpfiArr):
   global post_proc_file, build_count,extra_args,error_count,warning_count
   print("----build_product_from_info----")
   print("bpfiArr: " , bpfiArr)
   prod_id = bpfiArr.pop(0)
   print("prod_id: ", prod_id)
   format_filename = bpfiArr.pop(0)
   print("format_filename: ", format_filename)
   station_list = bpfiArr.pop(0)
   print("station_list: ", station_list)
   config_options = bpfiArr.pop(0)
   print("config_options: ", config_options)
   post_proc_file = bpfiArr.pop(0)

   print("global_format_time: ", global_format_time)
   global_format_time_Arr = []
   global_format_time_Arr.append(global_format_time)
   print("global_format_time_Arr: ", global_format_time_Arr)

   format_time = global_format_obj.as_text()
   print("format_time: ", format_time)

   build_count += 1

   print(f"building product {prod_id}")

   output_file = f"{output_dir}/{prod_id}"
   print("The output file will be: ", output_file)

   #
   # If our formatter name ends in .pl, then it is already a
   # perl program and can be used as is.
   #

   print("If our formatter name ends in .pl, then it is already a perl program and can be used as is.")
   print("format_filename = ", format_filename)
   format_filepath = f"{formatter_dir}/{format_filename}"
   perl_file = f"{formatter_pl_dir}/{format_filename}"
   perl_formatter = (re.match(r'\.pl$',format_filename))

   print("format_filepath: ", format_filepath)
   print("perl_file: ", perl_file)
   print("perl_formatter: ", perl_formatter)

   if  not perl_formatter:
      print(f"{format_filename}.pl not found")
      perl_file += '.pl'

   print("perl_file = ", perl_file)

   format_filepath_arr = []
   format_filepath_arr.append(format_filepath)
   print("format_filepath_arr: ", format_filepath_arr)

   print("Calling file_age ====>")
   formatter_age = file_age(format_filepath_arr)
   print("formatter_age: ", formatter_age)

   perl_file_arr = []
   perl_file_arr.append(perl_file)
   print(f"perl_file_arr = {perl_file_arr}")

   perl_age = file_age(perl_file_arr)
   print(f"perl_age = {perl_age}")

   if formatter_age == 'NO FILE':
      if perl_age == 'NO FILE':
         # fatal error, cannot format this product
         report_error(f"Formatter Error, could not build {prod_id}: Cannot find file {format_filepath}")
         error_count += 1
         return(0)

      # We have a Perl script but no source format file.
      report_error(f"Formatter Warning, building {prod_id}, Cannot find file {format_filepath}")
      warning_count += 1

   else:
      if perl_age == 'NO FILE' or perl_age > formatter_age:
         print(f"perl_formatter = {perl_formatter}")
         if perl_formatter:
            print(f"cp {format_filepath} {perl_file}")
            #os.system(f"cp {format_filepath} {perl_file}")

         else:
            # We need to build (or rebuild) the Python script.
            print(f"{base_path}/bin/make_python_formatter < {format_filepath} > {perl_file}")
            #os.system(f"{base_path}/bin/make_python_formatter < {format_filepath} > {python_file}")

         print(f'grep -v \"Failed to load locale\" {perl_file} > {perl_file}.tmp')
         #os.system(f'grep -v \"Failed to load locale\" {python_file} > {python_file}.tmp')

         print(f"mv {perl_file}.tmp {perl_file}")
         #os.system(f"mv {python_file}.tmp {python_file}")

         print(f"chmod +x  {perl_file}")
         #os.system(f"chmod +x  {python_file}")

         # check status and generage fatal error if new file
         # did not get built
         # os.access(python_file, os.X_OK)
         python_age = file_age(perl_file_arr)

         if (not os.access(perl_file, os.X_OK)) or perl_age == 'NO FILE' or perl_age > formatter_age:
            report_error(f"Formatter Error, could not build {prod_id}, Cannot build perl file")
            error_count += 1
            return(0)
   #
   # Build up the command line necessary for running the format script.
   #

   if config_options:
      default_match = re.match(r'-reltime +(-?[0-9]+)',config_options)
      if (default_match):
         relative_hour_offset = default_match.group(1)
         format_time = GFS_time.add_seconds(relative_hour_offset)

   if config_options:
      default_match = re.match(r'-gfs(.+)$',config_options)
      if (default_match):
         extra_args += default_match.group(1)


   # date_time_obj = datetime.datetime.strptime(format_time, '%Y-%m-%d %H:%M:%S.%f')
   print("format_time: ", format_time)
   time_fmt = "%Y-%m-%d %H:00:00"
   time_string = global_format_obj.as_text(time_fmt)
   format_cmdline = f"{perl_file} {station_list} '{time_string}' {extra_args}"
   print("format_cmdline: ", format_cmdline)

   if len(post_proc_file) > 0:
      post_proc_scripts = re.split(r' *\| *',post_proc_file)
      print("post_proc_scripts: ", post_proc_scripts)
      pp = None
      for pp in post_proc_scripts:
         default_match = re.match('([^ ]*) (.*)',pp)
         if (default_match):
            pp_com = default_match.group(1)
            pp_param = default_match.group(2)
         else:
            pp_com = pp
            pp_param = ''

         # report_error "command is /$pp_com/ params are /$2/\n";
         post_proc_path = f"{post_proc_dir}/{pp_com}"
         # check for presents and executability of post_proc file.
         # os.access(post_proc_path, os.X_OK)


         if not os.access(post_proc_path, os.X_OK):
            report_error(f"Formatter Error, could not build {prod_id}, missing post-proc file: {post_proc_path}")
            error_count += 1
            return(0)
         format_cmdline += f" | {post_proc_path} {pp_param} "
         print("format_cmdline: ", format_cmdline)

   format_cmdline += f" > {output_file}.TEMP"
   print("format_cmdline: ", format_cmdline)

   #
   # Issue the command to build into the .TEMP file. This way if
   # we are aborted, the previous output file will remain in place.
   #

   ipbArray = []
   ipbArray.append(prod_id)
   ipbArray.append(format_cmdline)
   print(f"ipbArray = {ipbArray}")
   #issue_product_build(ipbArray)

   #os.system(f"chmod g+w {output_file}.TEMP")

   #
   # Now that we are complete, move the old output file out of the way
   # and rename the TEMP file to the output file.
   # We must defer the abort between these two moves, otherwise we could
   # be left with no output file.
   # os.access('output_file', os.R_OK)

   disable_abort()
   if os.access(output_file, os.R_OK):
      print(f"mv {output_file} {old_output_dir}/{prod_id}")
      #os.system(f"mv {output_file} {old_output_dir}/{prod_id}")
   if os.access(f"{output_file}.TEMP", os.R_OK):
      print(f"mv {output_file}.TEMP {output_file}")
      #os.system(f"mv {output_file}.TEMP {output_file}")
   enable_abort()

   #fsize_Arr = []
   print("output_file: ",output_file)
   #fsize_Arr.append(output_file)
   fsize = os.stat(output_file).st_size
   print("fsize: ", fsize)

   if fsize > 0:
      build_time = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time()))
      print(f"""psql -h skybase-2-dev.cv9bnu4vuygm.us-east-1.rds.amazonaws.com gfsv10 postgres -c \"update product_generation_log set build_time = \'{build_time}\', filesize = {fsize} where product_name = \'{prod_id}\';\"""")
      #os.system(f"""psql -h skybase-2-dev.cv9bnu4vuygm.us-east-1.rds.amazonaws.com gfsv10 postgres -c \"update product_generation_log set build_time = \'{build_time}\', filesize = {fsize} where product_name = \'{prod_id}\';\"""")

   archive_cmd = f"{base_path}/bin/archive_product"
   print(f"{base_path}/bin/archive_product")
   if os.access(archive_cmd, os.X_OK):
      print(f"{archive_cmd} {output_file}")
      os.system(f"{archive_cmd} {output_file}")


build_product_from_info(bpfiArr)
