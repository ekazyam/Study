# idという組み込み関数はオブジェクト固有のIDを返却する
# この性質を利用してstring型のイミュータブル(変更不可)を検証する。

string_test = 'test1'

# IDが返却される。
print(id(string_test))

string_test = 'test2'

# 別の文字なので異なるIDが返却される。
print(id(string_test))

# 同じ値を代入する場合、同じメモリ領域が使われる可能性がある。
# これはメモリ節約に貢献している仕様である。
# ただし、必ずしも同じメモリ上のデータが扱われるかの保証はない。
string_test_1 = string_test_2 = 'test3'
print(id(string_test_1))
print(id(string_test_2))
