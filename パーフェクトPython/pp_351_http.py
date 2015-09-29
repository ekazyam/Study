#!/usr/bin/env python

import requests

res = requests.get('http://gihyo.jp/')

if res.status_code == requests.codes.ok:
    print(res)
