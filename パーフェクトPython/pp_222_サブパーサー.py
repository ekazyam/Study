#!/usr/bin/env python

import sys
import argparse


def greeting(arg):
    print("hello", arg)

pase = argparse.ArgumentParser()
sub_pases = pase.add_subparsers(dest="sub_name")
sub_pase = sub_pases.add_parser("greeting")
sub_pase.add_argument('-n', '--name', default="world")

arg = sub_pase.parse_args()


if not arg.sub_name:
    parser.print_help()
    sys.exit(1)

if args.sub_name == "greeting":
    greeting(arg)
