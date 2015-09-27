#!/usr/bin/env python

import sys
import argparse


pase = argparse.ArgumentParser()

pase.add_argument('-n', '--name', default="world")
pase.add_argument('-t', '--test', default="non_data")

arg = pase.parse_args()

print(arg.name, arg.test)
