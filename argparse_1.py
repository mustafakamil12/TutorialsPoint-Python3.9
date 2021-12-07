import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", required=False, action="store_true")
parser.add_argument("--cycle", help="parse cycle",required=False, action="store_true")
#parser.add_argument("-formatter", help="check formats on giving files", nargs="*", default="OXYOBSDAY", required=False, action="store_true")
parser.add_argument("--formatter", help="check formats on giving files", nargs="*", required=False)

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
elif args.cycle:
    print("working with cycle")
elif args.formatter:
    print("formatter...")
    print(args.formatter)
else:
    print("nor arg had been used")
