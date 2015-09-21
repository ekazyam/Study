#!/usr/bin/env python

import sys
import fileinput

while fileinput.FileInput(files=sys.argv[1:]) as f:
    for line in f:
        print(line)

if __name__ == '__main__':
    print('test')
