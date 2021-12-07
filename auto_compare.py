#!/usr/bin/python3
"""
    This compares textproduct files after running
       prod_build -product <textproduct>

    The script, prod_build, builds the commands to run textproduct and runs the commands.
    A normal build commands include the
        format perl script followed the post processing script.
"""
import argparse
import os
import time
import json
import subprocess
import sys
sys.path.append(".")
import shlex
import configparser
from pathlib import Path
from collections import namedtuple
from random import randint
from enum import IntEnum
import re,subprocess
from subprocess import PIPE
import threading
from threading import Thread, current_thread
from multiprocessing import Process, current_process
from compare_textproducts import *
import datetime
from datetime import date
from datetime import datetime
from detect_delimiter import detect

try:
    from csv_diff import load_csv, compare
    CSV_DIFF_AVAILABLE = True
except ModuleNotFoundError:
    CSV_DIFF_AVAILABLE = False
import csv

TextProductServer = namedtuple('Textproduct_Server',
                               ['host', 'user', 'base_path', 'prod_build_script'])


class CronTab(CompareProducts):

    def delimiter_cmp(self,a, b):
        #print("comparing ", a, " and ", b)
        if a == b:
            #print(0)
            return 0
        else:
            #print(-1)
            return -1

    def delimiter_compare(self,myfile_path):
        done = False
        no_of_lines = 1500
        myfile_path_lines_no = int(self.count_number_of_lines_in_file(myfile_path))
        if myfile_path_lines_no < 1500:
            with open(myfile_path,'r') as my_file:
                myfile = [next(my_file) for x in range(myfile_path_lines_no)]
        elif myfile_path_lines_no > 1500:
            with open(myfile_path,'r') as my_file:
                myfile = [next(my_file) for x in range(no_of_lines)]

        delimiter_array = []
        for line in myfile:
            #print(line)
            delimiter_detected = detect(line)
            #print(f"delimiter is = '{delimiter_detected}'")
            delimiter_array.append(delimiter_detected)
        for curr_index in range(len(delimiter_array)):
            for next_index in range(curr_index+1,len(delimiter_array)):
                comp_res = self.delimiter_cmp(delimiter_array[curr_index],delimiter_array[next_index])
                if comp_res == 0:
                    continue
                else:
                    print("Discover delmiter difference...")
                    done = True
                    break
            if done == True:
                #break
                return -1,'-1'
        my_file.close()
        return 0,delimiter_detected


    def crontab_periods_extractor(self):
        crontab_command = f"ssh {self.server2.user}@{self.server2.host} crontab -l | grep cycle"
        print(f"crontab_command = {crontab_command}")
        cronop = subprocess.run(crontab_command,stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        subprocess_rc = cronop.returncode
        #print(f"subprocess_rc{subprocess_rc}")
        cronop = cronop.stdout
        cronop = cronop.decode("utf-8")

        #print(f"cronop = {cronop}")
        cycle_payload = []
        cycle = re.findall(r'cycle .\S+',cronop)
        #print(f"cycle before cleaning = {cycle}")
        #print(f"the period of cycle in crontab {cycle}")
        for elem in cycle:
            #print(f"elem = {elem}")
            clean_cycle = elem.lstrip('cycle ')
            clean_cycle = clean_cycle.replace("'",'')
            #print(f"clean_cycle = {clean_cycle}")
            cycle_payload.append(clean_cycle.strip())

        #print(f"cycle_payload = {cycle_payload}")
        psqlcontArr = []
        psql_command = f"ssh {self.server2.user}@{self.server2.host}" + ' ' + "\"psql -A -t -c 'select distinct(period) from product_update_times '\""
        print(f"psql_command = {psql_command}")
        psqlPeriod = subprocess.run(psql_command,stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        subprocess_rc = psqlPeriod.returncode
        #print(f"subprocess_rc{subprocess_rc}")
        psqlPeriodop = psqlPeriod.stdout
        psqlPeriodop = psqlPeriodop.decode("utf-8")
        psqlcont = psqlPeriodop.splitlines()

        for elem in psqlcont:
            psqlcontelem = elem.rstrip()
            psqlcontArr.append(psqlcontelem.strip())
        #newpsqlcontArr =  psqlcontArr[2:]
        newpsqlcontArr =  psqlcontArr

        #psqlcontArr.pop(2)
        #newpsqlcontArr.pop(len(newpsqlcontArr)-1)
        #print(f"psqlcontArr = {newpsqlcontArr}")
        print(f"lenght of cycle_payload = {len(cycle_payload)}")
        print(f"length of psqlcontArr = {len(psqlcontArr)}")

        cycle_payload_as_set = set(cycle_payload)
        intersection = cycle_payload_as_set.intersection(psqlcontArr)
        intersection_as_list = list(intersection)
        print(f"length of intersection_as_list = {len(intersection_as_list)}")
        #print(intersection_as_list)
        return intersection_as_list


    def fetch_product_list_names_from_cycle_list(self,cycle_arr):
        #cycle_arr = ['ET_12PM']
        products_per_period = {}
        for cycle_elem in cycle_arr:
            print(f"cycle_elem = {cycle_elem}")
            prodcontArr = []
            psql_cmd = "select product_name from product_update_times where period = '%s' order by product_name" % cycle_elem
            cmd1 = "ssh %s@%s \"psql -A -t -c \\\"%s\\\"\" " % (self.server2.user, self.server2.host, psql_cmd)
            print(f"cmd1 = {cmd1}")

            cyclePeriodop = self.execute_get_result(cmd1)
            cyclecont = cyclePeriodop.splitlines()
            print(f"cyclecont = {cyclecont}")
            for elem in cyclecont:
                cyclecontelem = elem.rstrip()
                prodcontArr.append(cyclecontelem.strip())
            #newcyclecontArr =  prodcontArr[2:]
            newcyclecontArr =  prodcontArr

            #psqlcontArr.pop(2)
            #newcyclecontArr.pop(len(newcyclecontArr)-1)
            #newcyclecontArr.pop(len(newcyclecontArr)-1)
            print(
            f"newcyclecontArr = {newcyclecontArr}")

            products_per_period[cycle_elem] = []
            for newcyclecontArrelem in newcyclecontArr:
                products_per_period[cycle_elem].append(newcyclecontArrelem)

        print(f"products_per_period = {products_per_period}")
        return products_per_period

    def andromeda(self,period_dictionary):
        threadLock = threading.Lock()
        threads = []

        result_summary = {}
        start = time.time()
        for cycle_product_elem in period_dictionary:
            self.cron_period = cycle_product_elem
            for product_elem in period_dictionary[cycle_product_elem]:
                print(f"product = {product_elem}")
                #product_elem = 'CGCUOBS'
                i = 0
                # Get lock to synchronize threads
                threadLock.acquire()
                globals()[f"t{i}"] = Thread(target = self.fetch_and_compare, args =(product_elem, ))
                globals()[f"t{i}"].start()
                t_content = globals()[f"t{i}"]
                result_summary[product_elem] = t_content
                i += 1
                # Free lock to release next thread
                threadLock.release()
                # Add threads to thread list
                threads.append(t_content)

            # Wait for all threads to complete
            for t in threads:
                t.join()

        end = time.time()
        print('Time taken in seconds -', end - start)
        #testing = self.fetch_and_compare(product_elem)
        #print(testing)
        # print summary
        print("## Summary ##")
        for product_elem in result_summary:
            print("%s : %s" % (
                product_elem, "differ" if result_summary[product_elem] else "same"))


    def prepend_line(self,file_name, line):
        """ Insert given string as a new line at the beginning of a file """
        # define name of temporary dummy file
        dummy_file = file_name + '.bak'
        # open original file in read mode and dummy file in write mode
        with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Write given line to the dummy file
            write_obj.write(line + '\n')
            # Read lines from original file one by one and append them to the dummy file
            for line in read_obj:
                write_obj.write(line)
        # remove original file
        os.remove(file_name)
        # Rename dummy file as the original file
        os.rename(dummy_file, file_name)

    def count_number_of_lines_in_file(self,filepath):
        count = 0
        file = open(filepath, 'rb')
        while 1:
            buffer = file.read(8192*1024)
            decoded_buffer = buffer.decode('utf-8')
            #print(f"buffer = {decoded_buffer}")
            if not decoded_buffer: break
            #print(decoded_buffer.count('\n'))
            count += decoded_buffer.count('\n')
        #print(f"count = {count}")
        file.close()
        return count

    def execute_get_result(self,cmd):
        print(f"cmd will be run = {cmd}")
        cmdop = subprocess.run(cmd,stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        subprocess_rc = cmdop.returncode
        cmdop = cmdop.stdout
        cmdop = cmdop.decode("utf-8")
        # The output of this function is string
        return cmdop

    def compare_textproduct_files(self, textproduct_filepath1, textproduct_filepath2, diff_outputfile):
        """ compare text product using diff """
        diffcmd = "diff %s %s > %s" % (textproduct_filepath1, textproduct_filepath2, diff_outputfile)
        difflines_Num = "diff -y --suppress-common-lines %s %s | grep '^' | wc -l" % (textproduct_filepath1,textproduct_filepath2)
        if self.diff_type == DiffType.DIFF_LINES:
            print(diffcmd)
            os.system(diffcmd)
            file_size = os.path.getsize(diff_outputfile)
            if file_size > 0:
                self.work_dir = "/home/op/product_test/autodir"
                print(f"work directory = {self.work_dir}")
                today = date.today()
                now = datetime.now()
                today_date = today.strftime("%m/%d/%Y")
                time_now = now.strftime("%H:%M:%S")
                cmd = f"diff -y --suppress-common-lines {textproduct_filepath1} {textproduct_filepath2} | grep '^' | wc -l"
                print(f"cmd will be executed = {cmd}")
                compare_head_command = 'bash -c "diff <(head -n 2 %s) <(head -n 2 %s)"' % (textproduct_filepath1,textproduct_filepath2)
                print(f"compare_head = {compare_head_command}")
                number_of_diff_lines = int(self.execute_get_result(cmd))
                number_of_file1_lines = int(self.count_number_of_lines_in_file(textproduct_filepath1))
                number_of_file2_lines = int(self.count_number_of_lines_in_file(textproduct_filepath2))
                difference_percentage = number_of_diff_lines / number_of_file1_lines
                #print(f"number_of_diff_lines = {number_of_diff_lines}")
                #print(f"number_of_file1_lines = {number_of_file1_lines}")
                #print(f"difference_percentage = {difference_percentage}")
                file_size1 = os.path.getsize(diff_outputfile)
                file_size2 = os.path.getsize(diff_outputfile)
                textproduct_filename1 = re.findall(r'[^\\/:*?"<>|\r\n]+$',textproduct_filepath1)
                textproduct_filename2 = re.findall(r'[^\\/:*?"<>|\r\n]+$',textproduct_filepath2)
                diff_outputfilename = re.findall(r'[^\\/:*?"<>|\r\n]+$',diff_outputfile)
                compare_head_res = self.execute_get_result(compare_head_command)
                compare_head = "No"
                if compare_head_res != '':
                    compare_head = "Yes"


                line_to_add = ''
                line_to_add = "\n"
                line_to_add += f"Period: {self.cron_period} \n"
                line_to_add += ("-"*79 + "\n")
                line_to_add += f"|File Name: {diff_outputfilename[0]:33}|Date: {today_date:10} |Time: {time_now:8}|\n"
                line_to_add += ("-"*79 + "\n")
                line_to_add += f"\ncommand Used: {diffcmd} \n"
                line_to_add += "\nFiles participate in diff\n"

                line_to_add += ("-"*79 + "\n")
                line_to_add += f"|File Name:                                      |No. of Lines  |File size    |\n"
                line_to_add += ("-"*79 + "\n")
                line_to_add += f"|{textproduct_filename1[0]:48}|{number_of_file1_lines:^13} |{file_size1:^13}|\n"
                line_to_add += f"|{textproduct_filename2[0]:48}|{number_of_file2_lines:^13} |{file_size2:^13}|\n"
                line_to_add += ("-"*79 + "\n")

                line_to_add += ("-"*79 + "\n")
                line_to_add += f"|Number of different lines = {number_of_diff_lines: <20}| Is Head Differenet = {compare_head}    |\n"
                line_to_add += ("-"*79 + "\n")
                line_to_add += f"|Diff percentage = {difference_percentage: <59.0%}|\n"
                line_to_add += ("-"*79 + "\n")
                print(line_to_add)
                self.prepend_line(diff_outputfile, line_to_add)
                return 1
            return 0


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("textproduct_list", help="list of textproduct separated by comma",
                        nargs='*', default="OXYOBSDAY")
    parser.add_argument("-cycle", help="specify a cycle of textproducts to compare")
    parser.add_argument("-autocompare", help="compare all cycles' periods  in the crontab", required=False, action="store_true")
    parser.add_argument("-formatter", help="check formats on giving files", nargs="*", required=False)
    parser.add_argument("-testing", help="testing part of code in safe mode.", required=False, action="store_true")
    parser.add_argument("-difftype", help="diff types: 0 for diff, 1 for csv_diff, 2 for experimental diff",
                       required=False, type=int, default=0)
    parser.add_argument("-workdir", help="work directory to download product output",
                       required=False)
    parser.add_argument("-cleanup", help="clean up files after comparison",
                        required=False, action="store_true")
    parser.add_argument("-run_prod_build", help="run prod_build before comparison",
                        required=False, action="store_true")
    parser.add_argument("-v", "-verbose", help="verbose", required=False, action="store_true")


    args = parser.parse_args()
    # tolerance = float( args.tolerance )

    program_dir = os.path.dirname(str(Path(__file__).absolute()))

    if args.workdir is None:
        work_dir = os.path.join(program_dir, "workdir" )
        if not os.path.isdir(work_dir):
            print( "Making direcdtory, %s" % work_dir )
            os.makedirs(work_dir)
    else:
        work_dir = args.workdir

    configFile = os.path.join(program_dir, 'config', 'compare_config.ini')
    serverA, serverB = getTextProductServers(configFile)

    print( "Comparing prod_build output from these servers:")
    print( " ",serverA )
    print( " ",serverB )
    print( "Work directory %s" % work_dir)

    # Compare all cycles' periods in the crontab
    #print(f"args.autocompare = {args.autocompare}")
    if args.autocompare:
        #print("Testing -crontab option")
        crontab_cp = CronTab(serverA, serverB, work_dir, args.difftype, args.run_prod_build, args.cleanup)
        cron_tab_cycles_list = crontab_cp.crontab_periods_extractor()
        print(f"testList = {cron_tab_cycles_list}")
        cron_tab_cycles_dic = crontab_cp.fetch_product_list_names_from_cycle_list(cron_tab_cycles_list)
        #print(f"cron_tab_cycles_dic = {cron_tab_cycles_dic}")

        prod_not_in_periods_cmd = f"ssh {crontab_cp.server2.user}@{crontab_cp.server2.host} crontab -l | grep \"product_build_send -product\" | grep -v \"^#\" | sed -e \'s/.*product//g\' -e \"s/>.*//g\" -e \'s/,/ /g\'"
        prod_not_in_periods = crontab_cp.execute_get_result(prod_not_in_periods_cmd)
        prod_not_in_periods_list = prod_not_in_periods.split()
        print(f"prod_not_in_periods_list = {prod_not_in_periods_list}")

        prod_not_in_periods_dic = {}
        prod_not_in_periods_dic['No Period'] = prod_not_in_periods_list

        cron_tab_cycles_dic.update(prod_not_in_periods_dic)
        #print(f"cron_tab_cycles_dic = {cron_tab_cycles_dic}")

        prod_phoenix_not_in_periods_cmd = f"ssh {crontab_cp.server2.user}@{crontab_cp.server2.host} grep prod_build.py /pgs/bin/process* | sed -e \'s/.*product//g\'"
        prod_phoenix_not_in_periods = crontab_cp.execute_get_result(prod_phoenix_not_in_periods_cmd)
        prod_phoenix_not_in_periods_list_raw = prod_phoenix_not_in_periods.split()
        print(f"prod_phoenix_not_in_periods_list_raw = {prod_phoenix_not_in_periods_list_raw}")

        prod_phoenix_not_in_periods_list = []
        for phoenixElem in prod_phoenix_not_in_periods_list_raw:
            temp_array = phoenixElem.split(",")
            for phoenixSubElem in temp_array:
                prod_phoenix_not_in_periods_list.append(phoenixSubElem)

        print(f"prod_phoenix_not_in_periods_list = {prod_phoenix_not_in_periods_list}")

        prod_phoenix_not_in_periods_dic = {}
        prod_phoenix_not_in_periods_dic['Phoenix'] = prod_phoenix_not_in_periods_list

        cron_tab_cycles_dic.update(prod_phoenix_not_in_periods_dic)
        print(f"cron_tab_cycles_dic = {cron_tab_cycles_dic}")

        crontab_cp.andromeda(cron_tab_cycles_dic)
    elif args.testing:
        pass
    elif args.formatter:
        print(f"check file format for {args.formatter}")

        crontab_cp = CronTab(serverA, serverB, work_dir, args.difftype, args.run_prod_build, args.cleanup)
        if len(args.formatter) == 1:
            file_path_formatter_test = f"/home/op/product_test/autodir/{args.formatter[0]}"
            comp_res,comp_type = crontab_cp.delimiter_compare(file_path_formatter_test)
            if comp_res == 0:
                print(">>>>The format for the entier file is the same<<<<")
            else:
                print(">>>>The format for the entier file is not the same<<<<")
        elif len(args.formatter) > 1:
            comp_res_final = 0
            comp_res_arr = []
            for fname_elem in args.formatter:
                #print(fname_elem)
                file_path_formatter_test = f"/home/op/product_test/autodir/{fname_elem}"
                comp_res,comp_type = crontab_cp.delimiter_compare(file_path_formatter_test)
                if comp_res == 0:
                    comp_res_arr.append(comp_type)
                    continue
                else:
                    print(f">>>>Please advise There's format issue with {fname_elem}<<<<")
                    comp_res_final = -1
                    break

            #print(len(comp_res_arr))
            #print(comp_res_arr)
            done = False
            if comp_res_final == 0:
                for curr_index in range(len(comp_res_arr)):
                    for next_index in range(curr_index+1,len(comp_res_arr)):
                        comp_res_new = crontab_cp.delimiter_cmp(comp_res_arr[curr_index],comp_res_arr[next_index])
                        if comp_res_new == 0:
                            continue
                        else:
                            #print(">>>>Format is not the same on the given files<<<<")
                            done = True
                            break
                    if done == True:
                        comp_res_final = -1
                        break
                if done == False:
                    comp_res_final = 0
            if comp_res_final == 0:
                print(">>>>Files format matching<<<<")
            elif comp_res_final == -1:
                print(">>>>Files format not matching<<<<")

    else:

        # Get textproduct list from argument
        if args.cycle is not None:
            textproduct_list = fetch_text_product_list_names_from_cycle(serverB, args.cycle)
            if len(textproduct_list) == 0:
                print("Cycle %s did not return any product names" % args.cycle)
                sys.exit(1)
        else:
            textproduct_list = []
            for tpl in args.textproduct_list:
                textproduct_list.extend(tpl.split(","))
            if "allondir" in textproduct_list:
                textproduct_list = fetch_text_product_list_on_directory(serverB)

        if len(textproduct_list) == 0:
            print("one text product or a cycle text product needs to be specified.")
            sys.exit(1)
        print("List of textproduct(s) (count %d):" % len(textproduct_list))
        lineitems = []
        num = 0
        maxcols = 5
        for textproduct_name1 in textproduct_list:
            lineitems.append("%-20s" % textproduct_name1)
            num += 1
            if num % maxcols == 0:
                print("\t".join(lineitems))
                lineitems = []
        if len(lineitems) != 0:
            print("\t".join(lineitems))

        cp = CompareProducts(serverA, serverB, work_dir, args.difftype, args.run_prod_build, args.cleanup)

        result_summary = {}
        for textproduct_name1 in textproduct_list:
            result_summary[textproduct_name1] = cp.fetch_and_compare(textproduct_name1)

        # print summary
        print("## Summary ##")
        for textproduct_name1 in result_summary:
            print("%s : %s" % (
                textproduct_name1, "differ" if result_summary[textproduct_name1] else "same"))
