import sys,os,re,json,time
import fileinput,subprocess,inspect,datetime
from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool
from GFS_syslog import *
from GFS_timezone import *


GFS_DBI.initialise()

def report_error(errMsg):
    print("----report_error----")
    print(errMsg ,file=sys.stderr)
    #GFS_syslog.frmt_log_error(errMsg)
    frmt_log_error(errMsg)

def wait_for_process_slot():
    print("----wait_for_process_slot----")
    global process_limit
    process_slot = None
    print("process_limit: ", process_limit)

    while True:
        for process_slot in range(0,process_limit):
            if process_slots[process_slot] < 0:
                return(process_slot)

        if wait_for_children(1) < 1:
            return(-1)

def process_complete(processArr):
    print("----process_complete----")
    global start_time,prod_id_slot
    process_slot = processArr.pop(0)
    status = processArr.pop(0)
    end_time = time.time()
    print("process_slot: ", process_slot)
    print("status: ", status)
    print("end_time: ", end_time)

    min = int((end_time - start_time[process_slot]) / 60)
    sec = (end_time - start_time[process_slot]) - min * 60
    elapsed = '%02d:%02d' % ( min,sec)

    if status != 0:
        GFS_syslog.frmt_log_info(f"Completed product send for {prod_id_slot[process_slot]} with fatal error, {elapsed}")
        print(f"Completed product send for {prod_id_slot[process_slot]} with fatal error, {elapsed}")
        error_count += 1
    else:
        GFS_syslog.frmt_log_info(f"Completed product send for {prod_id_slot[process_slot]}, {elapsed}")
        print(f"Completed product send for {prod_id_slot[process_slot]}, {elapsed}")


def wait_for_children(wcfArr):
    print("----wait_for_children----")
    global process_slot,TIMEOUT_VALUE,process_slots,process_limit
    num_required = wcfArr
    print(f"num_required = {num_required}")
    print(f"process_limit = {process_limit}")
    print(f"TIMEOUT_VALUE = {TIMEOUT_VALUE}")
    if num_required > process_limit:
        num_required = process_limit

    print(f"num_required = {num_required}")
    for iteration in range(0,TIMEOUT_VALUE):
        print("iteration: ", iteration)
        num_free = 0
        for process_slot in range(0,process_limit):
            print(f"process_slots[process_slot] = {process_slots[process_slot]}")
            if process_slots[process_slot] < 0:
                num_free += 1
                continue
            pid, status = os.waitpid(process_slots[process_slot],os.WNOHANG)
            print(f"pid = {pid} and status = {status}")
            if pid != 0:
                processArr = []
                processArr.append(process_slot)
                processArr.append(status)
                process_complete(processArr)
                process_slots[process_slot] = -1
                num_free += 1
        print(f"num_free = {num_free}")
        if num_free >= num_required:
            return(num_free)
        time.sleep(1)

    return(0)


def send_product_from_info(spfiArr):
    print("----send_product_from_info----")
    #global error_count,send_count,start_time,process_slots
    #global start_time,prod_id_slot
    global send_count,error_count,start_time,prod_id_slot
    prod_id = spfiArr.pop(0)
    dist_type = spfiArr.pop(0)
    address = spfiArr.pop(0)
    post_proc = spfiArr.pop(0)

    print("prod_id: ", prod_id)
    print("dist_type: ", dist_type)
    print("address: ", address)
    print("post_proc: ", post_proc)

    address = ""
    send_count += 1

    # Use the prod_id to query for email addresses here. Combine the email addresses
    # into a comma-delimited list, followed by a space, and append the address from above.
    # The result will be what used to be in the address field in the database.

    if dist_type.upper() == 'Email'.upper() or dist_type.upper() == 'Attachment'.upper():
        # Use ssh to call a script hosted on energy-generic1. The script returns json
        # that contains the addresses.
        print('Retrieving addresses.')
        print(f'ssh -l op energy-generic1 \"~/api/call_api.pl {prod_id}\"')

        #json_str = f'ssh -l op energy-generic1 \"~/api/call_api.pl {prod_id}\"'
        json_Arr = [{"AddressId":"3e836a7f-d3b5-4a59-a78d-338313822e54","Type":"NA","Address":"godric.phoenix@gmail.com"}] # static addition by mustafa
        json_str = json_Arr[0] # this line will take info from the line above
        print("json_str: ", json_str)

        #json_hash = json.dumps(json_str)
        #print(f"json_hash = {json_hash}")

        addresses = []
        for key in json_str:
            print(f"{key} : {json_str[key]}")
            if key == "Address":
                addresses.append(json_str[key])

        print(f"addresses = {addresses}")
        # Prepend the comma-delimited email addresses to what came from the
        # address field in the database.

        if dist_type.upper() == 'Email'.upper():
            address = ",".join(addresses)
        else:
            address = ",".join(addresses) + ' ' + address

        print(f"address = {address}")

    file_to_send = f"{output_dir}/{prod_id}"

    if  not os.access(file_to_send, os.R_OK) :
        report_error(f"Cannot send file {file_to_send}, file not found")
        error_count += 1
        return()

    slot = wait_for_process_slot()
    print(f"slot = {slot}")
    if slot < 0:
        report_error ('Cannot send product: %s %s %s' % ( prod_id,dist_type,address))
        error_count += 1
        return()

    #
    # We need to handle certain substitutions in the string
    # we pass.
    #   1) the string may contain date macros such as %Y%h%M
    #      use the GFS_time package to substitute here
    #   2) If the string contains any dollar signs, we need
    #      to escape them via a backslash.
    #   3) If there are any pound signs or escaped dollar signs,
    #      then we need to enclose the word which contains them
    #      in a series of quotes. These quotes are designed to
    #      pass through two sets of csh invokations.
    #

    current_time = GFS_time([])
    print(f"current_time = {current_time}")
    offset = 0

    final_address = None
    print(f"address = {address}")

    if len(address) > 0:
        default_match = re.match('#TZ=(\w*)#',address)
        print(f"default_match = {default_match}")

        if (default_match):

            offset = GFS_timezone.get_timezone_offset([current_time.get_time_t(),default_match.group(1)])
            print(f"offset = {offset}")
            address = re.sub('#TZ=(\w*)#',"", address)
        final_address = current_time.as_text(address,offset)
        print(f"final_address = {final_address}")

    #print(f"before final test for final_address = {final_address}")
    if final_address:
        final_address = re.sub('\$','\\\$',final_address)
        final_address = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{final_address}\"\'\"\'\"\'" ,final_address)

    #
    # Now process the post processing command the same way we
    # processed the address.
    #

    final_post_proc = None
    if len(post_proc) > 0:
        offset = 0
"""
        default_match = re.match('#TZ=(\w*)#',post_proc)
        if (default_match.group(0)):
            offset = GFS_timezone.get_timezone_offset([current_time,default_match.group(1)])
            post_proc = re.sub('#TZ=(\w*)#',"",post_proc)
        final_post_proc = current_time.as_text(post_proc,offset)

    final_post_proc = re.sub('\$','\\\$',final_post_proc)
    final_post_proc = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{default_match.group(1)}\"\'\"\'\"\'" ,final_post_proc)

    short_address = final_address
    short_address = re.sub(' .*$',"",short_address)
    send_descriptor_print = prod_id + ' to ' + dist_type
    print('sending product %s',send_descriptor_print)

    send_descriptor = send_descriptor_print + ' ' + short_address

    cmd = f"{base_path}/bin/do_send {prod_id} {dist_type} \"{final_address}\" {file_to_send} '{final_post_proc}'"
    cmd_print = f"{base_path}/bin/do_send {prod_id} {dist_type} <address> {file_to_send} '{final_post_proc}'"

    #
    # We need to disable aborts until after the process has been
    # properly entered into the data structure.
    #
    disable_abort()

    pid = fork
    if pid:
        #print "started process pid in slot slot";
        GFS_timezone.start_time[slot] = time
        process_slots[slot] = pid
        #prod_id_slot[slot] = send_descriptor;
        prod_id_slot[slot] = send_descriptor_print
        GFS_syslog.frmt_log_info(f"Begin product send for {prod_id}, pid={pid}")
        GFS_syslog.frmt_log_info(f"Command for {prod_id} is {cmd}")
        print(f"Command for {prod_id} is {cmd_print}")
        enable_abort([])
        # wait for 2 seconds because the central facilities system
        # has a problem if two files are sent in the same second.
        sys.sleep(2)
    else:
        os.system(cmd)
"""

def send_products_for_cycle(spfcArr):
    global send_count
    print("----send_products_for_cycle----")

    print("spfcArr: ", spfcArr)
    cycle = spfcArr.pop(0)
    print("cycle: ", cycle)

    query = f"select product.product_name, destination_str, address, generic_distribution.post_proc from product,product_update_times, generic_distribution where product.product_name = product_update_times.product_name and product.product_name = generic_distribution.product_name and period = '{cycle}' and generic_distribution.enabled"
    print(f"select product.product_name, destination_str, address, generic_distribution.post_proc from product,product_update_times, generic_distribution where product.product_name = product_update_times.product_name and product.product_name = generic_distribution.product_name and period = '{cycle}' and generic_distribution.enabled")

    with CursorFromConnectionFromPool() as cursor:
        cursor.execute(query)
        row_ref = cursor.fetchall()

    print(f"row_ref = {row_ref}")
    row_ref_tup_to_list = []

    while row_ref:
        for elem in row_ref[0]:
            if isinstance(elem, datetime.date):
                selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
                row_ref_tup_to_list.append(selem)
                #print("row_ref_tup_to_list = ", row_ref_tup_to_list)
            else:
                row_ref_tup_to_list.append(elem)
                #print("row_ref_tup_to_list = ", row_ref_tup_to_list)

        print("row_ref_tup_to_list: ", row_ref_tup_to_list)

        #send_product_from_info(row_ref_tup_to_list)
        row_ref.pop(0)
        row_ref_tup_to_list = []


prod_id_slot = []
start_time = []
process_limit = 1
process_slots = [-1,-1,-1,-1]
TIMEOUT_VALUE = 5
base_path = '/Users/mustafaalogaidi/Desktop/MyWork'
output_dir = f"{base_path}/TutorialsPoint-Python3.9"
send_count = 0
error_count = 0
spfcArr = ['ET_01PM']
#send_products_for_cycle(spfcArr)

spfiArr = ['USEFCST', 'Attachment', '%Y%m%d%H.csv', None]
#spfiArr = ['BOFADLYFCSTN', 'Ftp', 'ftpsrv.wsicorp.com /u/ekt ekt pumpkin8ant NF%m%d%Y.txt', '']
send_product_from_info(spfiArr)
