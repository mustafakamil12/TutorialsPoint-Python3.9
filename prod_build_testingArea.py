import sys, re

argArr = sys.argv
argArr.pop(0)
argArrStr = ' '.join([str(singleArg) for singleArg in (argArr)])
print('Begin GFS formatting with parameters: ' + argArrStr)

arg = argArr.pop(0)
while arg:
   argRes = re.sub('^@','',arg)
   print("argRes: ", argRes)
   if argRes != arg:
      try:
         ARG_FILE = open(argRes,'w')
         arg = ARG_FILE.readline()
         arg = arg.rstrip("\n")
         argArr.insert(0,arg)
      except OSError:
         sys.exit()

   elif arg=='-cycle':
      build_cycle = 1
      cycle = argArr.pop(0)
      print(cycle)
   elif arg == '-customer':
      build_customer = 1
      customer_code = argArr.pop(0)
   elif arg == '-products' or arg == '-product':
      build_products = 1
      prod_list=re.split(',',argArr.pop(0))
      print(prod_list)
   elif arg == '-time':
      global_format_time = print(argArr.pop(0))
   elif arg == '-spawn':
      spawned = 1
   elif arg == '-gfs':
      # take rest of arguments and pass them in to formatter
      extra_args = sys.argv.join(' ')
      break
   if len(argArr) != 0:
       arg = argArr.pop(0)
   else:
       break
