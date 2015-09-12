# idという組み込み関数はオブジェクト固有のIDを返却する
# この性質を利用してstring型のイミュータブル(変更不可)を検証する。

string_test = 'test'

# IDが返却される。
print(id(string_test))

string_test = 'test2'

# 異なるIDが返却される。
print(id(string_test))

# 同じ値を代入する場合、同じメモリ領域が使われる可能性がある。
# これはメモリ節約に貢献している仕様である。
# ただし、必ずしも同じメモリ上のデータが扱われるかの保証はない。
string_test3 = 'test3'
string_test4 = 'test3'

print(id(string_test3))
print(id(string_test4))