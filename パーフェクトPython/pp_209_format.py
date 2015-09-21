#!/usr/bin/env python

# データを用意
data = 123456789

# 連想配列
array = {'key1': 2, 'key2': 5}

# リスト
list_data = [3, 6, 9]
list_data2 = [3, 4, 5]

# カンマ区切りで表示する。
print("{0:,}".format(data))
# 20桁表示で残りを0で埋める
print("{0:020}".format(data))

# 複数の値をフォーマットする。
print("{0:04} {1:02}".format(array['key1'], array['key2']))

# リストの値をフォーマットする。
print("{0:04} {1:02} {2:06}".format(list_data[0], list_data[1], list_data[2]))
