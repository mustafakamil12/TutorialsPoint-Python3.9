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
   print("post_proc_file: ", post_proc_file)


row_ref =  [('BOFADLYFCSTN', 'frmt_bofa_daily_fcst', 'bofa_stn', '', ''), ('SARACENOBS', 'obs_saracen', 'saracen_stn', None, ''), ('NGRID_LI', 'frmt_ngrid_li', 'single_FRG', None, ''), ('USEFCST', 'frmt_usenergy', 'usenergy_stn', None, ''), ('DTEHOURLYFCST', 'frmt_dtehourly', 'dte_new_stn', None, '')]

prod_count = 0
prod_name = []
print("row_ref = ", row_ref)

while row_ref:
   #print("row_ref.pop(0): ", row_ref[0])
   #print("prod_count: ", prod_count)
   row_ref_tup_to_list = [elem for elem in row_ref[0]]
   prod_name.append(prod_count)
   prod_name.append(row_ref_tup_to_list[0])

   print("row_ref_tup_to_list: ", row_ref_tup_to_list)
   build_product_from_info(row_ref_tup_to_list)
   print("row_ref_tup after pass it to build_product_from_info: ", row_ref_tup_to_list)

   print("prod_name: ", prod_name)
   prod_count += 1
   row_ref.pop(0)

print("prod_count: ", prod_count)
