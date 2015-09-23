#!/usr/bin/env python

f = open('./pp_213_行の分割.csv')

for line in f:
	parts = line.split(",")

for data in parts:
	print(data)

f.close()
