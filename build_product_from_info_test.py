import sys,os,re,time
from GFS_time import *

global_format_time =  1626133797
global_format_obj = GFS_time('')
global_format_time = global_format_obj.get_time_t()


row_ref_tup_to_list = ['DTEHOURLYFCST', 'frmt_dtehourly', 'dte_new_stn', None, '']

def build_product_from_info(bpfiArr):
   global post_proc_file, build_count,extra_args
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

   format_time = global_format_obj.as_text([])
   print("format_time: ", format_time)
"""
   build_count += 1

   print(f"building product {prod_id}")

   output_file = f"{output_dir}/{prod_id}"
   print("The output file will be: ", output_file)

   #
   # If our formatter name ends in .pl, then it is already a
   # perl program and can be used as is.
   #
   format_filepath = f"{formatter_dir}/{format_filename}"
   python_file = f"{formatter_py_dir}/{format_filename}"
   python_formatter = (re.match(r'\.pl$',format_filename))

   print("format_filepath: ", format_filepath)
   print("python_file: ", python_file)
   print("python_formatter: ", python_formatter)


   if  not python_formatter:
      python_file += '.pl'

   format_filepath_arr = []
   format_filepath_arr.append(format_filepath)
   print("format_filepath_arr: ", format_filepath_arr)
   formatter_age = file_age(format_filepath_arr)
   print("formatter_age: ", formatter_age)

   python_file_arr = []
   python_file_arr.append(python_file)
   print("python_file_arr: ", python_file_arr)
   python_age = file_age(python_file_arr)
   print("python_age: ", python_age)

   error_count = 0 # reset this counter for testing purposes
   warning_count = 0

   if formatter_age == 'NO FILE':
      if python_age == 'NO FILE':
         # fatal error, cannot format this product
         report_error(f"Formatter Error, could not build {prod_id}: Cannot find file {format_filepath}")
         error_count += 1
         return(0)
      # We have a python script but no source format file.
      report_error(f"Formatter Warning, building {prod_id}, Cannot find file {format_filepath}")
      warning_count += 1
   else:
      if python_age == 'NO FILE' or python_age > formatter_age:
         if python_formatter:
            print(f"cp {format_filepath} {python_file}")
            os.system(f"cp {format_filepath} {python_file}")
         else:
            # We need to build (or rebuild) the Python script.
            print(f"{base_path}/bin/make_python_formatter < {format_filepath} > {python_file}")
            os.system(f"{base_path}/bin/make_python_formatter < {format_filepath} > {python_file}")

         print(f'grep -v \"Failed to load locale\" {python_file} > {python_file}.tmp')
         os.system(f'grep -v \"Failed to load locale\" {python_file} > {python_file}.tmp')

         print(f"mv {python_file}.tmp {python_file}")
         os.system(f"mv {python_file}.tmp {python_file}")

         print(f"chmod +x  {python_file}")
         os.system(f"chmod +x  {python_file}")

         # check status and generage fatal error if new file
         # did not get built
         # os.access(python_file, os.X_OK)
         python_age = file_age(python_file_arr)
         if (not os.access(python_file, os.X_OK)) or python_age == 'NO FILE' or python_age > formatter_age:
            report_error(f"Formatter Error, could not build {prod_id}, Cannot build perl file")
            error_count += 1
            return(0)

   #
   # Build up the command line necessary for running the format script.
   #
   if config_options:
      default_match = re.match(r'-reltime +(-?[0-9]+)',config_options)
      if (default_match.group(0)):
         relative_hour_offset = default_match.group(1)
         format_time = GFS_time.add_seconds(relative_hour_offset)

   if config_options:
      default_match = re.match(r'-gfs(.+)$',config_options)
      if (default_match(0)):
         extra_args += default_match.group(1)
   # date_time_obj = datetime.datetime.strptime(format_time, '%Y-%m-%d %H:%M:%S.%f')
   print("format_time: ", format_time)
   time_arr = []
   time_arr.append('%Y-%m-%d %H:00:00')
   time_string = global_format_obj.as_text(time_arr)
   format_cmdline=f"{python_file} {station_list} '{time_string}' {extra_args}"
   print("format_cmdline: ", format_cmdline)

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
         # report_error "command is /$pp_com/ params are /$2/\n";
         post_proc_path=f"{post_proc_dir}/{pp_com}"
         # check for presents and executability of post_proc file.
         # os.access(post_proc_path, os.X_OK)
         if  not os.access(post_proc_path, os.X_OK):
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
   issue_product_build([prod_id,format_cmdline])

   os.system(f"chmod g+w {output_file}.TEMP")

   #
   # Now that we are complete, move the old output file out of the way
   # and rename the TEMP file to the output file.
   # We must defer the abort between these two moves, otherwise we could
   # be left with no output file.
   # os.access('output_file', os.R_OK)

   disable_abort()
   if os.access(output_file, os.R_OK):
      os.system(f"mv {output_file} {old_output_dir}/{prod_id}")
   if os.access(f"{output_file}.TEMP", os.R_OK):
      os.system(f"mv {output_file}.TEMP {output_file}")
   enable_abort()

   #fsize_Arr = []
   print("output_file: ",output_file)
   #fsize_Arr.append(output_file)
   fsize = os.stat(output_file).st_size
   print("fsize: ", fsize)

   if fsize > 0:
      build_time = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time()))


   archive_cmd = f"{base_path}/bin/archive_product"
   print(f"{base_path}/bin/archive_product")
   if os.access(archive_cmd, os.X_OK):
      os.system(f"{archive_cmd} {output_file}")

"""

build_product_from_info(row_ref_tup_to_list)
