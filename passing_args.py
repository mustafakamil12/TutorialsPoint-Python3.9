#!/usr/bin/python3


import argparse

def myfunction(myNum):
    print(f"the passing number is {myNum}")

my_parser = argparse.ArgumentParser(description='Testing The Usage Of Arguments')

my_parser.add_argument("-n", help="an integer for the accumulator")

args = my_parser.parse_args()

if args.n is not None:
    myfunction(args.n)
#print(f"my_parser = {my_parser}")
