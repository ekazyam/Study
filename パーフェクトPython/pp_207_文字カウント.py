#!/usr/bin/env python
with open('./pp_204_readtest.txt') as f:
    count = 0
    search = input()
    for line in f:
        if line.find(search) != -1:
            print('data is find.')

f = open('./pp_204_readtest.txt')
for line in f:
    if line.find(search) != -1:
        print(line, ' is find at original ', line.find(search))
f.close()
