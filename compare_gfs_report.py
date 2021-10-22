#!/usr/bin/python3
"""
    This compares the output files after running gfs_report on two systems.

    Each system runs gfs_report with three inputs:
        1) station list name, ( e.g. phoenix_na_stn )
        2) base time ( e.g. '08Oct21 17:00' )
        3) measurement input parameter file ( e.g./tmp/param_in.20674 )

    For example,
        {base_path}/bin/gfs_report.py phoenix_na_stn '08Oct21 17:00'  < /tmp/param_in.20674 > /tmp/gfs_report.output

    The report generates an output that can be save to a file.   The output file is compared to
    another output file, that is generated from running gfs_report on another system.  The three inputs to gfs_report
    should be the same.

    This script will compare the values and report how many values are not similar within tolerance.
"""

import sys
import argparse
import os
import time
import subprocess
import shlex
import configparser
from pathlib import Path
from datetime import datetime
from random import randint
from collections import namedtuple

GFSReportServer = namedtuple('GFSreport_Server',
                               ['host', 'user', 'base_path', 'gfs_report', 'work_dir'])

InputServerParameters = namedtuple('InputServerParameter', [
    'input_filepath',
    'output_filepath',
    'fetch_output_filepath' ]
    )

InputParameter = namedtuple('Input_Parameter',
                             ['station_list', 'input_filename'])


class CompareGFSreport:

    def __init__(self, server1, server2, program_dir1, work_dir1, verbose1=False):
        self.server1 = server1
        self.server2 = server2
        self.program_dir = program_dir1
        self.work_dir = work_dir1
        self.verbose = verbose1

    def run_fetch_compare(self, station_list_name1, base_time1, input_filename1, tolerance1=0.001, measurement=None):
        fetch_rc, file1, file2 = self.run_fetch2(station_list_name1, base_time1, input_filename1)
        if fetch_rc == 0:
            self.compare_gfs_report(file1, file2, tolerance1, measurement)

    def run_fetch(self, station_list_name1, base_time1, input_filename1):
        """
            The run command the gfs_report on the remote servers.   It does the following:
                1) upload the input files to the remove server
                2) run the gfs_report with input parameters and the input file, via ssh
                   and stores the output on the remove server
                3) downloads the output of gfs_report locally
                4) remove the output of gfs_report remotely
        """
        print("#" * 80)
        print(datetime.now())
        print("    Running gfs_report ( %s, %s, %s)" % (station_list_name1, base_time1, input_filename1))
        print("#" * 80)

        base_name = os.path.basename(input_filename1)

        server1_output_base_name = base_name.replace("_in", "_out") + "_" + self.server1.host
        server2_output_base_name = base_name.replace("_in", "_out") + "_" + self.server2.host
        server1_file_param = InputServerParameters(
            os.path.join(self.server1.work_dir, base_name),
            os.path.join(self.server1.work_dir, server1_output_base_name),
            os.path.join(self.work_dir, server1_output_base_name)
            )
        server2_file_param = InputServerParameters(
            os.path.join(self.server2.work_dir, base_name),
            os.path.join(self.server2.work_dir, server2_output_base_name),
            os.path.join(self.work_dir, server2_output_base_name)
            )
        # the command could be pipe to ssh and record output

        commands = []
        commands.append("scp -p %s %s@%s:%s" % (
            os.path.join(self.program_dir, input_filename1), self.server1.user, self.server1.host,
            server1_file_param.input_filepath))
        commands.append("scp -p %s %s@%s:%s" % (
            os.path.join(self.program_dir, input_filename1), self.server2.user, self.server2.host,
            server2_file_param.input_filepath))
        commands.append("ssh %s@%s \"%s %s '%s' < %s > %s\" " % (
            self.server1.user, self.server1.host, os.path.join(self.server1.base_path, self.server1.gfs_report),
            station_list_name1, base_time1, server1_file_param.input_filepath, server1_file_param.output_filepath))
        commands.append("ssh %s@%s \"%s %s '%s' < %s > %s\" " % (
            self.server2.user, self.server2.host, os.path.join(self.server2.base_path, self.server2.gfs_report),
            station_list_name1, base_time1, server2_file_param.input_filepath, server2_file_param.output_filepath))
        commands.append("scp -p %s@%s:%s %s" % (
            self.server1.user, self.server1.host,
            server1_file_param.output_filepath, server1_file_param.fetch_output_filepath))
        commands.append("scp -p %s@%s:%s %s" % (
            self.server2.user, self.server2.host,
            server2_file_param.output_filepath, server2_file_param.fetch_output_filepath))
        commands.append("ssh %s@%s \"rm -f %s %s\"" % (
            self.server1.user, self.server1.host,
            server1_file_param.input_filepath, server1_file_param.output_filepath))
        commands.append("ssh %s@%s \"rm -f %s %s\"" % (
            self.server2.user, self.server2.host,
            server2_file_param.input_filepath, server2_file_param.output_filepath))

        execcmds_rc = 0
        for cmd in commands:
            print("  %s" % cmd)
            maxtries = 3
            scp_rc = -1
            tries = 0
            while scp_rc != 0 and tries < maxtries:
                completedprocess = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
                scp_rc = completedprocess.returncode
                if scp_rc != 0:
                    sleeptime = randint(10, 60)
                    print("  Trying again after %d seconds" % sleeptime)
                    time.sleep(sleeptime)
                tries += 1
            if tries == maxtries:
                print("  Failed")
                execcmds_rc = -1

        return execcmds_rc, server1_file_param.fetch_output_filepath, server2_file_param.fetch_output_filepath

    def run_fetch2(self, station_list_name1, base_time1, input_filename1):
        """
            This utilizes subprocess input argument to feed data the ssh command and stdout to fetch the output.  The
            advantage is that number of commands are lower and simpler, but it may be harder to debug issues as the
            communication and data are in transitions throughout the process.

            stdout is captured for data comparison.
        """
        print("#" * 80)
        print(datetime.now())
        print("    Running gfs_report ( %s, %s, %s)" % (station_list_name1, base_time1, input_filename1))
        print("#" * 80)

        base_name = os.path.basename(input_filename1)

        server1_output_base_name = base_name.replace("_in", "_out") + "_" + self.server1.host
        server2_output_base_name = base_name.replace("_in", "_out") + "_" + self.server2.host

        commands = []
        commands.append(
            [ "ssh %s@%s \"%s %s '%s' \" " % (
                self.server1.user, self.server1.host, os.path.join(self.server1.base_path, self.server1.gfs_report),
                station_list_name1, base_time1),
                os.path.join(self.work_dir, server1_output_base_name)
             ]
            )
        commands.append(
            [ "ssh %s@%s \"%s %s '%s' \" " % (
                self.server2.user, self.server2.host, os.path.join(self.server2.base_path, self.server2.gfs_report),
                station_list_name1, base_time1),
                os.path.join(self.work_dir, server2_output_base_name)
             ]
            )

        print("  Input file: %s" % input_filename1)
        # read input data
        with open(os.path.join(self.program_dir, input_filename1), 'rb') as input_f:
            data = input_f.read()

        execcmds_rc = 0
        gfs_report_runtime = []
        for cmd in commands:
            maxtries = 3
            scp_rc = -1
            tries = 0
            print("  %s" % cmd)
            perf_time1 = time.perf_counter()
            while scp_rc != 0 and tries < maxtries:

                completedprocess = subprocess.run(shlex.split(cmd[0]), input=data,
                                                  stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False)
                scp_rc = completedprocess.returncode
                if scp_rc != 0:
                    sleeptime = randint(10, 60)
                    print("  Trying again after %d seconds" % sleeptime)
                    time.sleep(sleeptime)
                else:
                    with open(cmd[1], 'w') as output_f:
                        for line in completedprocess.stdout.decode():
                            output_f.write(line)
                tries += 1
            if tries == maxtries:
                print("  Failed")
                execcmds_rc = -1
            perf_time2 = time.perf_counter()
            elapse_time = perf_time2 - perf_time1
            gfs_report_runtime.append(elapse_time)
        print( "Elapse times (seconds) ", gfs_report_runtime )
        return execcmds_rc, commands[0][1], commands[1][1]

    def compare_gfs_report(self, file1, file2, tolerance1=0.001, measurement=None):
        print("%s Comparing two gfs_reports: %s %s" % (datetime.now(), file1, file2))
        mdata1 = self.read_file(file1)
        mdata2 = self.read_file(file2)

        # compare  gfs_report files
        if measurement is not None:
            mkey1 = args.measurement
            if mkey1 not in mdata1:
                print("  mkey, %s, is not found in file, %s" % (mkey1, args.file1))
                sys.exit(1)
            if mkey1 not in mdata2:
                print("  mkey, %s, is not found in file, %s" % (mkey1, args.file2))
                sys.exit(1)

            mvalues1 = mdata1[mkey1]
            mvalues2 = mdata2[mkey1]

            is_text = mkey1.find("Text") != -1
            comp_rc = self.compare_values(
                mkey1, mvalues1, mvalues2, tolerance1, is_text, self.verbose)

        else:
            for mkey1, mvalues1 in mdata1.items():
                # print("mvalue ", mvalues1)

                if mkey1 not in mdata2:
                    print("  mkey, %s, is not found in file, %s" % (mkey1, args.file2))
                    continue

                mvalues2 = mdata2[mkey1]

                is_text = mkey1.find("Text") != -1
                comp_rc = self.compare_values(
                    mkey1, mvalues1, mvalues2, tolerance1, is_text, self.verbose)
        return comp_rc

    def read_file(self, filename):
        print("Reading file, %s" % filename)
        data = {}
        with open(filename) as rfh:
            for line in rfh:
                idx = line.find('&')
                if idx == -1:
                    continue
                terms = line.strip().split('&')
                data[ terms[0] ] = terms[1:]
        return data

    def compare_values(self, mkey1, mvalues1, mvalues2,
                      tolerance1=0.0001, is_text=False, verbose=False,):
        measurement_pass = True
        count_above_tolerance = 0
        sum_above_tolerance = 0.0

        result = []

        value2Word = {
                 0: "ok same value",
                 1: "ok within tolerance",
                 2: "ok with no data",
                 -1: "not ok"
        }
        if is_text:  # if the values are text
            for idx, v1 in enumerate(mvalues1):
                v2 = mvalues2[idx]
                if v1 == v2:
                    values_same = 0
                else:
                    count_above_tolerance += 1
                    values_same = -1
                    measurement_pass = False

                if verbose:
                    result.append((v1, v2, values_same))

        else:  # if the values are float
            sum_above_tolerance = 0.0
            no_data = [ -1000000020040877342720.000000, -1000000000000000000000.000000, -99999997781963083612160.000000 ]
            for idx, v1 in enumerate(mvalues1):
                v2 = mvalues2[idx]
                values_same = 0

                if float(v1) in no_data and float(v2) in no_data:  # if the values are no value
                    values_same = 2
                elif float(v1) == float(v2):
                    values_same = 0
                elif abs(float(v1) - float(v2)) <= tolerance1:
                    values_same = 1
                    sum_above_tolerance += abs(float(v1) - float(v2))
                else:
                    values_same = -1
                    sum_above_tolerance += abs(float(v1) - float(v2))
                    count_above_tolerance += 1
                    measurement_pass = False

                if verbose:
                    result.append((v1, v2, values_same))

        # print result
        print("mkey %s ( %d/%d had failed, Overall %s,  tolerance average %f )" % (
                    mkey1,
                    count_above_tolerance, (idx + 1),
                    ("ok" if measurement_pass else "not ok"),
                    sum_above_tolerance / (idx + 1)
        ))

        if verbose:
            for idx, row in enumerate(result):
                print("%d) %s, %s %s" % (
                        idx, row[0], row[1],
                        value2Word[ row[2] ]
                    ))

        return measurement_pass


def get_gfs_report_servers(config_file):
    config_data = configparser.ConfigParser()
    config_data.read(config_file)

    server_a = config_data['ServerA']
    server_b = config_data['ServerB']

    grs_a = GFSReportServer(server_a['host'], server_a['user'], server_a['base_path'], server_a['gfs_report_script'], "/tmp")
    grs_b = GFSReportServer(server_b['host'], server_b['user'], server_b['base_path'], server_b['gfs_report_script'], "/tmp")

    return grs_a, grs_b


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-files", help="two gfs_report output files to compare", nargs=2, metavar=('file1', 'file2'))
    group.add_argument("-input_name", help="input parameter name ( supported PHOENIXDAILYFCST, PHOENIXHOURLYFCST ). Run the executor for other parameter names")

    parser.add_argument("-base_time", help="base time for the forecast")
    parser.add_argument("-workdir", help="work directory to download gfs_report",
                       required=False)
    parser.add_argument("-m", "--measurement", help="measurement key: e.g. WIND CHILL:Fahrenheit:16", required=False)
    parser.add_argument("-t", "--tolerance", help="tolerance level for numeric values", required=False, default=0.0001)
    parser.add_argument("-verbose", help="verbose", required=False, action="store_true")

    args = parser.parse_args()
    tolerance = float(args.tolerance)

    program_dir = os.path.dirname(str(Path(__file__).absolute()))

    if args.workdir is None:
        work_dir = os.path.join(program_dir, "workdir")
        if not os.path.isdir(work_dir):
            print("Making directory, %s" % work_dir)
            os.makedirs(work_dir)
    else:
        work_dir = args.workdir

    configFile = os.path.join(program_dir, 'config', 'compare_config.ini')
    serverA, serverB = get_gfs_report_servers(configFile)

    input_dict = {
        'PHOENIXDAILYFCST': InputParameter('phoenix_na_stn',
                                           'data/gfs_report/param_in.PHOENIXDAILYFCST'),
        'PHOENIXHOURLYFCST': InputParameter('phoenix_na_stn',
                                            'data/gfs_report/param_in.PHOENIXHOURLYFCST')
        }
    if args.input_name is not None:
        if args.input_name not in input_dict:
            print("I do not have input parameters for %s" % args.input_name)
            sys.exit(1)

    print("Comparing gfs_report output from these servers:")
    print(" server A", serverA)
    print(" server B", serverB)
    print(" tolerance %f" % tolerance)
    print(" measurement %s" % args.measurement)
    print(" Working directory: %s" % work_dir)

    cgr = CompareGFSreport(serverA, serverB, program_dir, work_dir, args.verbose)

    if args.files is not None:
        cgr.compare_gfs_report(args.files[0], args.files[1], tolerance, args.measurement)
    else:
        station_list_name = input_dict[args.input_name].station_list
        if args.base_time is None:
            dtn = datetime.utcnow()
            base_time = dtn.strftime("%d%b%y %H:00")
        else:
            base_time = args.base_time
        input_filename = input_dict[args.input_name].input_filename
        cgr.run_fetch_compare(station_list_name, base_time, input_filename,
                              tolerance, args.measurement)

    sys.exit(0)
