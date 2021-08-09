import sys,os,re,json,time
import fileinput,subprocess,inspect,datetime
import GFS_timezone
import GFS_syslog
from GFS_DBI import *
from GFS_DBI import CursorFromConnectionFromPool
from GFS_syslog import *
from GFS_timezone import *

GFS_DBI.initialise()

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


def report_error(errMsg):
    print("----report_error----")
    print(errMsg ,file=sys.stderr)
    #GFS_syslog.frmt_log_error(errMsg)
    frmt_log_error(errMsg)


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
    if post_proc != None and len(post_proc) > 0:
        offset = 0

        default_match = re.match('#TZ=(\w*)#',post_proc)
        if (default_match):
            offset = GFS_timezone.get_timezone_offset([current_time.get_time_t(),default_match.group(1)])
            post_proc = re.sub('#TZ=(\w*)#',"",post_proc)
        final_post_proc = current_time.as_text(post_proc,offset)

    if final_post_proc:
        final_post_proc = re.sub('\$','\\\$',final_post_proc)
        final_post_proc = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{final_post_proc}\"\'\"\'\"\'" ,final_post_proc)

    short_address = final_address
    print(f"short_address = {short_address}")
    short_address = re.sub(' .*$',"",short_address)
    send_descriptor_print = prod_id + ' to ' + dist_type
    print('sending product ',send_descriptor_print)

    send_descriptor = send_descriptor_print + ' ' + short_address
    print(f"send_descriptor = {send_descriptor}")

    cmd = f"{base_path}/bin/do_send {prod_id} {dist_type} \"{final_address}\" {file_to_send} '{final_post_proc}'"
    print(f"cmd = {cmd}")
    cmd_print = f"{base_path}/bin/do_send {prod_id} {dist_type} <address> {file_to_send} '{final_post_proc}'" # Need to check do_send script ... Mustafa
    print(f"cmd_print = {cmd_print}")

    #
    # We need to disable aborts until after the process has been
    # properly entered into the data structure.
    #
    disable_abort()

    pid = os.fork()

    if pid:
        #print("started process pid in slot slot")
        print(f"start_time = {start_time}")
        print(f"slot = {slot}")
        start_time.insert(slot,time)
        print(f"process_slots = {process_slots}")
        process_slots[slot] = pid
        print(f"process_slots = {process_slots}")
        print(f"prod_id_slot = {prod_id_slot}")
        prod_id_slot.insert(slot,send_descriptor_print)
        print(f"prod_id_slot = {prod_id_slot}")

        GFS_syslog.frmt_log_info(f"Begin product send for {prod_id}, pid={pid}")
        GFS_syslog.frmt_log_info(f"Command for {prod_id} is {cmd}")
        print(f"Command for {prod_id} is {cmd_print}")
        enable_abort()
        # wait for 2 seconds because the central facilities system
        # has a problem if two files are sent in the same second.
        os.system('sleep 2')
    else:
        os.system(cmd)


def send_products_for_customer(spfArr):
    print("----send_products_for_customer----")
    cust_id = spfArr.pop(0)

    query = 'select product.product_name, destination_str, address, generic_distribution.post_proc from ' + f"product, generic_distribution where customer_code = '{cust_id}' " + 'and product.product_name = generic_distribution.product_name and ' + 'generic_distribution.enabled'

    with CursorFromConnectionFromPool() as cursor:
        cursor.execute(query)
        row_ref = cursor.fetchall()

    #print(row_ref)
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
        #row_ref_tup_to_list.insert(0,prod_id)
        send_product_from_info(row_ref_tup_to_list)
        row_ref.pop(0)
        row_ref_tup_to_list = []


send_count = 0
error_count = 0
pending_abort = 0
prod_id_slot = []
start_time = []
process_limit = 1
process_slots = [-1,-1,-1,-1]
TIMEOUT_VALUE = 5
base_path = '/Users/mustafaalogaidi/Desktop/MyWork'
output_dir = f"{base_path}/TutorialsPoint-Python3.9"

customer_code = "VITOL"
#print('select product.product_name, destination_str, address, generic_distribution.post_proc from ' + f"product, generic_distribution where customer_code = '{cust_id}' " + 'and product.product_name = generic_distribution.product_name and ' + 'generic_distribution.enabled')

customer_codeArr = []
customer_codeArr.append(customer_code)
print(f"customer_codeArr = {customer_codeArr}")

send_products_for_customer(customer_codeArr)
