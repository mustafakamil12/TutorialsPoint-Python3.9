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
import shlex
import configparser
from pathlib import Path
from collections import namedtuple
from random import randint
from enum import IntEnum
try:
    from csv_diff import load_csv, compare
    CSV_DIFF_AVAILABLE = True
except ModuleNotFoundError:
    CSV_DIFF_AVAILABLE = False
import csv

TextProductServer = namedtuple('Textproduct_Server',
                               ['host', 'user', 'base_path', 'prod_build_script'])


class DiffType(IntEnum):
    DIFF_LINES = 0  # use external diff
    DIFF_CSV = 1  # use csv_diff, if possible
    DIFF_EXPERIMENTAL = 2  # experimatal


class CompareProducts:

    def __init__(self, server1, server2, work_dir1, diff_type=0,
                 run_prod_build=False, cleanup_files=False):
        self.server1 = server1
        self.server2 = server2
        self.work_dir = work_dir1
        self.diff_type = diff_type
        self.run_prod_build = run_prod_build
        self.clean_files = cleanup_files

    def run_textproduct_on_server(self, textproduct_name):
        """ run prod_build script on servers """
        cmd1 = "ssh %s@%s %s -product %s" % (
            self.server1.user, self.server1.host,
            os.path.join(self.server1.base_path, "bin", self.server1.prod_build_script), textproduct_name)

        cmd2 = "ssh %s@%s %s -product %s" % (
            self.server2.user, self.server2.host,
            os.path.join(self.server2.base_path, "bin", self.server2.prod_build_script), textproduct_name)

        print(cmd1)
        os.system(cmd1)
        print(cmd2)
        os.system(cmd2)

    def fetch_textproduct_files(self, textproduct_name):
        """ fetch text product from servers """
        textproduct_path1 = os.path.join(self.work_dir, "%s.%s" % (textproduct_name, self.server1.host))
        cmd1 = "scp -p %s@%s:%s %s" % (
            self.server1.user, self.server1.host,
            os.path.join(self.server1.base_path, "text_products", textproduct_name), textproduct_path1)

        textproduct_path2 = os.path.join(self.work_dir, "%s.%s" % (textproduct_name, self.server2.host))
        cmd2 = "scp -p %s@%s:%s %s" % (
            self.server2.user, self.server2.host,
            os.path.join(self.server2.base_path, "text_products", textproduct_name), textproduct_path2)

        print(cmd1)
        maxtries = 3
        scp_rc = -1
        tries = 0
        while scp_rc != 0 and tries < maxtries:
            completedprocess = subprocess.run(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            scp_rc = completedprocess.returncode
            if scp_rc != 0:
                sleeptime = randint(10, 60)
                print("  Trying again after %d seconds" % sleeptime)
                time.sleep(sleeptime)
            tries += 1
        if tries == maxtries:
            print("  Failed to download the file, %s" % textproduct_path1)
        # os.system(cmd1)

        print(cmd2)
        scp_rc = -1
        tries = 0
        while scp_rc != 0 and tries < maxtries:
            completedprocess = subprocess.run(shlex.split(cmd2), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            scp_rc = completedprocess.returncode
            if scp_rc != 0:
                sleeptime = randint(10, 60)
                print("  Trying again after %d seconds" % sleeptime)
                time.sleep(sleeptime)
            tries += 1
        if tries == maxtries:
            print("  Failed to download the file, %s" % textproduct_path2)
        # os.system(cmd2)

        return textproduct_path1, textproduct_path2

    def compare_textproduct_files(self, textproduct_filepath1, textproduct_filepath2, diff_outputfile):
        """ compare text product using diff """
        diffcmd = "diff %s %s > %s" % (textproduct_filepath1, textproduct_filepath2, diff_outputfile)
        if self.diff_type == DiffType.DIFF_LINES:
            print(diffcmd)
            os.system(diffcmd)
            file_size = os.path.getsize(diff_outputfile)
            if file_size > 0:
                return 1
            return 0

        if self.diff_type == DiffType.DIFF_CSV:  # using csv_diff requires a key in the csv or tsv file.
            if CSV_DIFF_AVAILABLE == False:
                print("  Could not use csv_diff, fallback to diff by lines" )
                print(diffcmd)
                os.system(diffcmd)
                file_size = os.path.getsize(diff_outputfile)
                if file_size > 0:
                    return 1
                return 0

            print("csv-diff %s %s   output: %s" % (
                 textproduct_filepath1, textproduct_filepath2, diff_outputfile
                ))
            diff = compare(
                load_csv(open(textproduct_filepath1)),
                load_csv(open(textproduct_filepath2))
            )

            with open(diff_outputfile, "w") as out:
                # pprint.pprint(diff, out, 4)
                out.write(json.dumps(diff, indent=4))

            return diff["added"] + diff["removed"] + diff["changed"]

        if self.diff_type == DiffType.DIFF_EXPERIMENTAL:
            print("experimental diff %s %s   output: %s" % (
                 textproduct_filepath1, textproduct_filepath2, diff_outputfile
                ))

            return_value = -1
            dialect = None
            with open(textproduct_filepath1, "r") as csvfile:
                csvfile.seek(0)
                peek = csvfile.read(1024 ** 2)
                try:
                    dialect = csv.Sniffer().sniff(peek, delimiters=",\t;")
                except csv.Error:
                    pass
            if dialect is None:
                print("  Could not determine delimiter from file, %s.  fallback to diff by lines" % textproduct_filepath1)
                print(diffcmd)
                os.system(diffcmd)
                file_size = os.path.getsize(diff_outputfile)
                if file_size > 0:
                    return 1
                return 0

            return_value = -1
            csv1 = []
            csv2 = []
            with open(textproduct_filepath1, "r") as csvfile:
                csvreader = csv.reader(csvfile, dialect)
                for row in csvreader:
                    csv1.append(row)
            with open(textproduct_filepath2, "r") as csvfile:
                csvreader = csv.reader(csvfile, dialect)
                for row in csvreader:
                    csv2.append(row)

            with open(diff_outputfile, "w") as out:
                if len(csv1) != len(csv2):
                    out.write("The files differ in number of rows")
                    out.write("%s has %d rows" % (textproduct_filepath1, len(csv1)))
                    out.write("%s has %d rows" % (textproduct_filepath2, len(csv2)))
                    return_value = 1
                else:
                    # the same number of rows, compare each rows
                    # assumption is the rows are output in the same order on each system
                    elem_num_count = 0
                    elem_match_count = 0
                    for row_num, rowline1 in enumerate(csv1):
                        # print( row_num, rowline1 )
                        # print( row_num, csv2[row_num])
                        rowline2 = csv2[row_num]
                        elem_not_match = []
                        for i in range(len(rowline1)):
                            if rowline1[i] != rowline2[i]:
                                try:
                                    elem_num1 = float(rowline1[i])
                                except ValueError:
                                    elem_num1 = None
                                try:
                                    elem_num2 = float(rowline2[i])
                                except ValueError:
                                    elem_num2 = None
                                if elem_num1 is None or elem_num2 is None:
                                    elem_not_match.append(i)
                                else:
                                    if abs(elem_num1 - elem_num2) > 5:
                                        elem_not_match.append(i)
                                    else:
                                        tolerance_match = True
                                        elem_match_count += 1
                            else:
                                elem_match_count += 1
                            elem_num_count += 1
                        if len(elem_not_match) != 0:
                            out.write("differ on row %d element position(s) %s\n" % (
                                row_num, elem_not_match))
                    if elem_num_count != elem_match_count:
                        out.write("the text product differs " +
                              "with tolerance\n" if tolerance_match else "\n")
                        out.write("Number of elements match %d / %d (%f percentage)\n" % (
                            elem_match_count, elem_num_count, elem_match_count / elem_num_count
                            ))
                        return_value = 2
                    else:
                        out.write("the text product are same " +
                              "with tolerance\n" if tolerance_match else "\n")
                        return_value = 0
            return return_value

        print("Diff method is not specified")
        return -1

    def clean_textproduct_files(self, textproduct_filepath1, textproduct_filepath2):
        """ remove text product locally """
        cmd3 = "rm %s %s" % (textproduct_filepath1, textproduct_filepath2)
        print(cmd3)
        os.system(cmd3)

    def fetch_and_compare(self, textproduct_name):
        """ fetch and compare a text product """
        print("#" * 80)
        print("   Comparing textproduct %s" % textproduct_name)
        print("#" * 80)

        if self.run_prod_build:
            self.run_textproduct_on_server(textproduct_name)
        textproduct_filepath1, textproduct_filepath2 = self.fetch_textproduct_files(textproduct_name)
        diff_outputfile = os.path.join(self.work_dir, "%s.diffs" % (textproduct_name))
        result = self.compare_textproduct_files(textproduct_filepath1, textproduct_filepath2, diff_outputfile)
        if self.clean_files:
            self.clean_textproduct_files(textproduct_filepath1, textproduct_filepath2)
        return result


def fetch_text_product_list_on_directory(server):
    """ fetch a list of text products by running 'ls' """
    cmd1 = "ssh %s -l %s ls %s " % (server.host, server.user, os.path.join(server.base_path, "text_products"))
    print("Fetching a list of product names from directory on %s " % server.host)
    print("   %s" % cmd1)
    completedprocess = subprocess.run(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return completedprocess.stdout.decode("UTF-8").split()


def fetch_text_product_list_names_from_cycle(server, cycle):
    """ fetch a list of text products by running a database query """
    # select_query = "select product_name from product_generation_log where build_start > now() - interval '7 days' order by build_start desc"
    select_query = "select product_name from product_update_times where period = '%s' order by product_name" % cycle
    cmd1 = "ssh %s@%s \"psql -A -t -c \\\"%s\\\"\" " % (
        server.user, server.host, select_query)
    print("Fetching a list of product names on cycle, %s, from database on %s " % (
        cycle, server.host))
    print("   %s" % cmd1)
    completedprocess = subprocess.run(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return completedprocess.stdout.decode("UTF-8").split()


def getTextProductServers(config_file):
    configData = configparser.ConfigParser()
    configData.read(config_file)

    server_a = configData['ServerA']
    server_b = configData['ServerB']

    tps_a = TextProductServer(server_a['host'], server_a['user'], server_a['base_path'], server_a['prod_build_script'])
    tps_b = TextProductServer(server_b['host'], server_b['user'], server_b['base_path'], server_b['prod_build_script'])

    return tps_a, tps_b


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("textproduct_list", help="list of textproduct separated by comma",
                        nargs='*', default="OXYOBSDAY")
    parser.add_argument("-cycle", help="specify a cycle of textproducts to compare")
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
