#!/usr/bin/env python
import msgpack
import pickle
import json

data1 = dict()

data1['spam'] = 'egg'
data1['スパム'] = '卵'
data1['ham'] = [1.0, 2, 3]

packed_data1 = msgpack.packb(data1)
pickle_data1 = pickle.dumps(data1)
jsoned_data1 = json.dumps(data1)


print(packed_data1)
print(jsoned_data1)
print(pickle_data1)

unpacked_data1 = msgpack.unpackb(packed_data1, encoding='utf-8', use_list=True)
print(unpacked_data1)
