







while argArr:
    print("inside while loop...")
    arg = argArr.pop(0)
    argRes = re.sub('^@','',arg)
    print("argRes: ", argRes)
    print("arg: ", arg)
    if argRes != arg:
        try:
            ARG_FILE = open(argRes,'w')
            arg = ARG_FILE.readline()
            arg = arg.rstrip("\n")
            argArr.insert(0,arg)
        except OSError:
            sys.exit()
        
    elif arg == '-cycle':
        send_cycle = 1
        cycle = argArr.pop(0)
        print("cycle: ", cycle)
    elif arg == '-customer':
        send_customer = 1
        customer_code = argArr.pop(0)
        print("customer_code: ", customer_code)
    elif arg == '-products' or arg == '-product':
        send_products = 1
        prod_list = re.split(',',argArr.pop(0))
        print("prod_list: ", prod_list)

    if len(argArr) != 0:
        arg = argArr.pop(0)
        arg = argArr[0]
        print("next arg to be used: ", arg)
    else:
        break

print("check send_cycle if it's defined")
try:
   send_cycle
   print("send_cycle is defined")
   cycleArr = []
   cycleArr.append(cycle)
   print("cycleArr: " , cycleArr)
   send_products_for_cycle(cycleArr)
except:
   print("send_cycle is not defined")
   
print("check send_customer if it's defined")
try:
  send_customer
  print("send_customer is defined")
  customer_codeArr = []
  customer_codeArr.append(customer_code)
  send_products_for_customer(customer_codeArr)
except:
  print("send_customer is not defined")    


print("check send_products if it's defined")
try:
   send_products
   print("send_products is defined")
   for product_id in prod_list:
      product_idArr = []
      product_idArr.append(product_id)
      print("product_idArr: ", product_idArr)
      send_product_from_name(product_idArr)
except:
   print("send_products is not defined")



if wait_for_children(process_limit) != process_limit:
    print(file=sys.stderr)
    #
    # force an error completion for all outstanding processes.
    #
    for process_slot in range(0, process_limit - 1):
        if process_slots[process_slot] < 0:
            continue 
        process_complete([process_slot,-1])

if send_cycle:
    official_tag = 'official'
    official_history_column = 'official_table'
    prod_send_update_column = 'product_send_time'

    cycle_time_Arr = []
    cycle_time_Arr.append(official_history_column)
    cycle_time_Arr.append(official_tag)
    print("cycle_time_Arr: ", cycle_time_Arr)

    cycle_time = GFS_history.get_cycle_time(cycle_time_Arr)

    time_string = GFS_date.format_date(GFS_date.current_date_time())
    print("time_string: ", time_string)

    print("------------------------")
    print("cycle_time: ", cycle_time)
    print("prod_send_update_column: ", prod_send_update_column)
    print("time_string: ", time_string)

    
    update_history_row_Arr = []
    update_history_row_Arr.append(cycle_time) 
    update_history_row_Arr.append(prod_send_update_column)
    update_history_row_Arr.append(time_string)

    print("update_history_row_Arr: ", update_history_row_Arr)

    GFS_history.update_history_row(update_history_row_Arr)

    print(f"GFS Product send complete {send_count} products, {error_count} errors, {warning_count} warnings")

"""
if __name__ == "__main__":
    print("Prod_Send.py")
"""