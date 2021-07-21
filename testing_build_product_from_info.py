from GFS_time import *

bpfiArr =  ['BOFAHRLYFCST12AM', 'frmt_bofa_hourly_fcst', 'bofa_stn', '', '']
global_format_obj = GFS_time([])
global_format_time = global_format_obj.get_time_t()
build_count = 0
base_path = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9'
output_dir = f"{base_path}/text_products"
formatter_dir = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9"
formatter_pl_dir = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/format_files_pl"
error_count = 0
warning_count = 0
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

#--------------------------------------------------------------------------------------------------
def report_error(errMsg):
   print("----report_error----")
   print(errMsg ,file=sys.stderr)
   #GFS_syslog.frmt_log_error(errMsg)


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
         if perl_formatter:
            print(f"cp {format_filepath} {perl_file}")
            os.system(f"cp {format_filepath} {perl_file}")


build_product_from_info(bpfiArr)
