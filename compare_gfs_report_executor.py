#!/usr/bin/python3
"""
    This program supports executing compare_gfs_report
    The script, compare_gfs_report, requires three parameters to run: station list name, base time and
    measurement input parameter file. Normally, the formatter script generates these these parameters before
    calling the gfs_report.   In this script, the three parameters are provided here, and are passed
    the gfs_report on each system.

    Two parameters, station_list_name and measurement input parameter file, are stored in a config file,
    input_param_file.csv.   The parameters to run gfs_report are selected from command argument passed to
    the script.  The command argument must be one of the following:
       run <input parameter name.
       run_all
       run_random_all
       run_random <number>
"""
import os
import csv
import sys
import argparse
import random
from datetime import datetime
from pathlib import Path
from collections import namedtuple

program_dir = os.path.dirname(str(Path(__file__).absolute()))
sys.path.insert(0, program_dir)
from compare_gfs_report import CompareGFSreport, get_gfs_report_servers

InputParameter = namedtuple('Input_Parameter',
                             ['station_list', 'input_filename'])


class CompareGFSreportExecutor:

    def __init__(self, input_file, base_time1, program_dir1, work_dir1, verbose1):
        self.input_file = input_file
        self.input_dict = self.read_input_file()
        self.base_time = base_time1
        self.program_dir = program_dir1
        self.work_dir = work_dir1
        self.verbose = verbose1
        config_file = os.path.join(program_dir, 'config', 'compare_config.ini')
        self.serverA, self.serverB = get_gfs_report_servers(config_file)
        if self.verbose:
            print(self.serverA)
            print(self.serverB)

    def read_input_file(self):
        input_dict = {}
        with open(self.input_file) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                # print(', '.join(row))
                if row[0].startswith("#"):  # skip
                    continue
                input_dict[row[0]] = InputParameter(row[1], row[2])
        return input_dict

    def run(self, cmd):
        if cmd[0] == 'list':
            self.list_input_parameter()
        elif cmd[0] in [ 'run', 'run_all', 'run_random_all', 'run_random' ]:
            if cmd[0] == 'run':
                if len(cmd) == 1:
                    print("specify input names to run ")
                    sys.exit(1)
                else:
                    input_name_list = cmd[1].split(',')
            else:
                if cmd[0] == 'run_all':
                    input_name_list = self.input_dict.keys()
                elif cmd[0] == 'run_random_all':
                    input_name_list = list(self.input_dict.keys())
                    random.shuffle(input_name_list)
                elif cmd[0] == 'run_random':
                    if len(cmd) == 1:
                        print("specify a number to run")
                        sys.exit(1)
                    try:
                        num = int(cmd[1])
                    except:
                        print("%s is not a number" % cmd[1])
                        sys.exit(1)
                    input_name_list = list(self.input_dict.keys())
                    random.shuffle(input_name_list)
                    input_name_list = input_name_list[0:num]

            if self.verbose:
                print("List of input name(s) to run")
                print(input_name_list)

            cgr = CompareGFSreport(self.serverA, self.serverB, self.program_dir,
                                   self.work_dir, self.verbose)

            for name in input_name_list:
                station_list_name = self.input_dict[name].station_list
                if self.base_time is None:
                    dtn = datetime.utcnow()
                    base_time = dtn.strftime("%d%b%y %H:00")
                else:
                    base_time = args.base_time
                input_filename = self.input_dict[name].input_filename
                cgr.run_fetch_compare(station_list_name, base_time, input_filename)
            print("Done")
            sys.exit(0)
        else:
            print("Operator command, %s, is unknown" % cmd[0])
            sys.exit(1)

    def list_input_parameter(self):
        # print(self.input_dict)
        elem = []
        max_col = 5
        for idx, name in enumerate(self.input_dict):
            # print( name )
            elem.append("%-22s" % name)

            if idx % max_col == max_col - 1:
                print("".join(elem))
                elem = []
        if len(self.input_dict) % max_col < max_col - 1:
            print("".join(elem))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("command", help="one of operator cmds: list, run, run_all, run_random, run_random_all",
                        nargs='*')
    parser.add_argument("-input_file", help="input parameter file",
                         default="config/input_param_file.csv")
    parser.add_argument("-workdir", help="work directory to download gfs_report",
                       required=False)
    parser.add_argument("-base_time", help="base time for the forecast; eg. '20Oct21 01:00'")
    parser.add_argument("-verbose", help="verbose", required=False, action="store_true")

    args = parser.parse_args()

    program_dir = os.path.dirname(str(Path(__file__).absolute()))
    if args.workdir is None:
        work_dir = os.path.join(program_dir, "workdir")
        if not os.path.isdir(work_dir):
            print("Making directory, %s" % work_dir)
            os.makedirs(work_dir)
    else:
        work_dir = args.workdir

    gce = CompareGFSreportExecutor(args.input_file, args.base_time, program_dir,
                                   work_dir, args.verbose)
    gce.run(args.command)
    print("Done")
