# バイト配列型を利用すると、ミュータブルなデータ型(同一オブジェクトはメモリ上で変更が許容される)
# データはバイナリデータである。

ba1 = bytearray()
ba1.append(115)
print(ba1)
