#!/usr/bin/python3
# $Revision: /main/19 $ $Modtime: 02/06/28 12:16:59 $ $Author: bwp $
#-----------------------------------------------------------------------------
#
# gfs_report.C
#
# GFS_forecast class implementation
#
# COPYRIGHT 2001 WSI
#
#-----------------------------------------------------------------------------

# This program takes as standard input lines of the form
#  PARAMETER:UNITS:forecast_period
# where PARAMETER is the parameter name as defined in
# the GFS_forecast class.
# Units is the unit name as defined in the WWMeasure class
# appropriate to the parameter
# and forecast_period is the number of hours from the base time.

# Command line parameters are the station list name followed
# by the base time.

# The output of the program is text of the form:
#
# input_file&value1&value2&value3...
#
# were value1, value2, value3 ... are the values for the parameter
# and time for each station in the station list.
import sys
import os
from pathlib import Path

env_var_name = "GFS_BASE_OVERRIDE"

if env_var_name in os.environ:  # production:  base directory of gfs files
    GFS_BASE = os.environ[env_var_name]
else:
    GFS_BASE = "/pgs"
libdir = os.path.join(GFS_BASE, "lib")  #              location of lib directory under base
if not os.path.exists(libdir):
    print("Python lib directory, %s, is not present " % libdir, file=sys.stderr)
    # development env: set pythonlib in path to run in command line or
    #                  define pythonlib directory in project properties)
    # libdir = os.path.join( "..", 'pythonlib' )
    libdir = os.path.join(str(Path(__file__).parent.absolute()), '..', 'pythonlib')
    print("  Using python lib directory, %s " % libdir, file=sys.stderr)
sys.path.insert(0, os.path.join(libdir, 'gfs_common'))
sys.path.insert(0, os.path.join(libdir, 'support'))
sys.path.insert(0, os.path.join(libdir, 'nc_util'))

from timstr import Met_time_string
from gfs_report_procedure import GFS_report_procedure

def usage():
    lines = []
    lines.append("Usage: %s <station list> <base time> <source> <options>\n\n" % sys.argv[0])
    lines.append("Where <source> is optional, can be one of:\n\n")
    lines.append("   -official (default)               official DB partition\n")
    lines.append("   -working                          working DB partition\n")
    lines.append("   -preliminary                      preliminary DB partition\n")
    lines.append("   -table <table name>               arbitrary DB partition\n")
    lines.append("   -netcdf <NetCDF file> <map table> load from NetCDF\n\n")
    lines.append("Time format is ddmmmyy hh:mm\n")
    lines.append("   valid options are:  -import <import filename>\n")
    print("".join(lines), file=sys.stderr)
    sys.exit(-1)


if __name__ == "__main__":
    args = sys.argv

    # parse command arguments
    if len(sys.argv) < 3:
        usage()

    # Read station list name
    argidx = 1
    station_list_name = sys.argv[argidx]

    # Second argument should be base time
    argidx += 1
    met_time = Met_time_string(sys.argv[argidx])
    time_rc, base_time = met_time.get_time()
    if not time_rc:
        print ("Illegal time: %s" % sys.argv[argidx], file=sys.stderr)
        sys.exit(-1)

    source_elem = []
    option_elem = []

    fix_day_boundaries_spikes = False
    argidx += 1
    if argidx < len(sys.argv):
        # Figure out where to load from
        if sys.argv[argidx] == "-netcdf":
            argidx += 1
            netCDFfile = sys.argv[argidx]
            argidx += 1
            mapping_table = sys.argv[argidx]
            source_elem = [ "-netcdf", netCDFfile, mapping_table ]
        elif sys.argv[argidx] in [ "-preliminary", "-dicast", "-working" ]:
            source_elem = [ sys.argv[argidx] ]  # tableprefix is parsed later
        elif sys.argv[argidx] == "-table":
            argidx += 1
            table_name = sys.argv[argidx] + "_"
        elif sys.argv[argidx] == "-official":
            argidx -= 1
        argidx += 1

    #
    # Check for -import argument
    #
    import_file = ""
    if argidx < len(sys.argv) and sys.argv[argidx] == "-import":
        argidx += 1
        import_file = sys.argv[argidx]
        option_elem = [ "-import", import_file ]
        argidx += 1

    grp = GFS_report_procedure()
    grp.run(station_list_name, base_time, source_elem, option_elem, fix_day_boundaries_spikes)
