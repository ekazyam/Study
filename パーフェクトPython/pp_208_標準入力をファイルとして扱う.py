#!/usr/bin/env python
import sys


def echo2(in_, out):
    for line in in_:
        out.write(line)

echo2(sys.stdin, sys.stdout)
