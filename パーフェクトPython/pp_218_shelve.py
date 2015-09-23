#!/usr/bin/env python

import shelve

# shelveでデータを保存する
# データを保存する
db = shelve.open("data_storedata_store", "c")
print(len(db))
