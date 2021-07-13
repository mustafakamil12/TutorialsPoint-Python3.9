import psycopg2
import os
import subprocess

import GFS_DBI
from GFS_DBI import CursorFromConnectionFromPool

def build_products_for_cycle(bpfcArray):
    global build_count
    print("----build_products_for_cycle----")
    print("input arguments: " ,bpfcArray)
    #global extra_args,spawned,dbh,global_format_time,build_count
    cycle = bpfcArray.pop(0)

    print('select product.product_name, format_descriptor_filename, station_list, ' + 'config_options, post_proc_script from ' + 'product,product_update_times ' + 'where product.product_name = product_update_times.product_name ' + f"and period = '{cycle}'")
    query = 'select product.product_name, format_descriptor_filename, station_list, ' + 'config_options, post_proc_script from ' + 'product,product_update_times ' + 'where product.product_name = product_update_times.product_name ' + f"and period = '{cycle}'"

    with CursorFromConnectionFromPool() as cursor:
      cursor.execute(query)
      row_ref = cursor.fetchall()

    prod_count = 0
    prod_name = []

    print("row_ref = ", row_ref)
    row_ref_tup_to_list = []
    while row_ref:
        for elem in row_ref[0]:
            if isinstance(elem, datetime.date):
                selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
                row_ref_tup_to_list.append(selem)
            else:
                row_ref_tup_to_list.append(elem)

        prod_name.append(prod_count)
        prod_name.append(row_ref_tup_to_list[0])

        print("row_ref_tup_to_list: ", row_ref_tup_to_list)
        build_product_from_info(row_ref_tup_to_list)
        print("row_ref_tup after pass it to build_product_from_info: ", row_ref_tup_to_list)

        print("prod_name: ", prod_name)
        prod_count += 1
        row_ref.pop(0)
        row_ref_tup_to_list = []


    print("prod_name = ", prod_name)

    if prod_count % 2 == 0:
        num_spreads = prod_count / 2
    else:
        num_spreads=(prod_count + (2 - (prod_count % 2))) / 2

    print("num_spreads: ", num_spreads)
    cur_prod = 0

    for x in range(0,num_spreads):
        print("x: ", x)
        try:
            BACKLOG = open('ps -ef | grep spawn | grep -v grep | wc -l |','w')
        except OSError:
            sys.exit()
        data = BACKLOG.readline()
        BACKLOG.close()
        data=re.sub(r'\s','',data)


        while data >= 6:
            os.system('sleep 2')
            try:
                BACKLOG=open('ps -ef | grep spawn | grep -v grep | wc -l |','w')
            except OSError:
                sys.exit()
            data = BACKLOG.readline()
            BACKLOG.close()
            data = re.sub(r'\s','',data)
            # print("Backlog = ",data)
            data += 1

        y = 0
        while y < 2 and cur_prod < prod_count:
            print(f"/data/gfs/v10/bin/prod_build.pl -product {prod_name[cur_prod]} -spawn &")
            os.system(f"/data/gfs/v10/bin/prod_build.pl -product {prod_name[cur_prod]} -spawn &")
            cur_prod += 1
            y += 1
        os.system('sleep 1')

    try:
        BACKLOG = open('ps -ef | grep spawn | grep -v grep | wc -l |','w')
    except OSError:
        sys.exit()
    data = BACKLOG.readline()
    BACKLOG.close()
    data = re.sub(r'\s','',data)


    while data >= 1:
        os.system('sleep 1')
        try:
            BACKLOG = open('ps -ef | grep spawn | grep -v grep | wc -l |','w')
        except OSError:
            sys.exit()
        data = BACKLOG.readline()
        BACKLOG.close()
        data = re.sub(r'\s','',data)

    build_count = prod_count

build_products_for_cycle(['ET_01PM'])
