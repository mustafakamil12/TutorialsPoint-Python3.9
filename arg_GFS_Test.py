import sys,os,re

argArr = sys.argv
print("argArr: ", argArr)

argArr.pop(0)
argArrStr = ' '.join([str(singleArg) for singleArg in (argArr)])
print("arg list as string: " , argArrStr)
print("argArr after removing script name: ", argArr)

arg = argArr.pop(0)
print("argArr after pop up first element: ", argArr)
print("arg before while and it's the first element: ", arg)


while arg:
   argRes = re.sub('^@','',arg)
   print("argRes: ", argRes)
   if  argRes != arg:
      try:
          ARG_FILE = open(argRes,'w')
          arg = ARG_FILE.readline()
          arg = arg.rstrip("\n")
          argArr.insert(0,arg)
      except OSError:
         sys.exit()
   elif arg == '-cycle':
      print("check cycle...")
      build_cycle = 1
      cycle = argArr.pop(0)
   elif arg == '-customer':
      print("check customer...")
      build_customer = 1
      customer_code = argArr.pop(0)
   elif arg == '-products' or arg == '-product':
      print("check products or product...")
      build_products = 1
      prod_list=re.split(',',argArr.pop(0))
      print("prod_list: ", prod_list)
   elif arg == '-time':
      print("check time...")
      #global_format_time = GFS_time(sys.argv.pop(0))
      print("will get time information...")
   elif arg == '-spawn':
      print("check spawned...")
      spawned = 1
   elif arg == '-gfs':
      print("check gfs...")
      # take rest of arguments and pass them in to formatter
      extra_args = sys.argv.join(' ')
      break
   if len(argArr) != 0:
       arg = argArr.pop(0)
   else:
       break
