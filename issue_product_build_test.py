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
