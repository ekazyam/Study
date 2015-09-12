
def ite():
	array = [ 1, 2, 3, 4, 5, 6]

	for i in array:
		# 順次アクセスしてくれる
		print(i)

def ite2():
	array = [ 1, 2, 3, 'abcde']

# forに渡す型がリストになっていれば良いので、以下の記載も可能
	for s in array[3]:
		# 文字を分解して出力してくれる
		print(s)

def ite3():
	array = [ 1, 2, 3, 4 ]
	array.append(5)
	print(array)

# 要素の削除
def ite4():
	array = [ 1, 2, 3, 4 ]
	array.remove(2)
	print(array)

# 要素の反転
def ite5():
	array = [ 1, 2, 3, 4 ]
	array.reverse()
	print(array)

# 要素の更新
def ite6():
	array = [ 1, 2, 3, 4 ]
	array[0] = 5
	print(array)

# 要素のソート
def ite7():
	array = [ 2,6,1,3,8 ]
	# ミュータブルなので、arrayオブジェクトそのものがソートされる
	array.sort()
	print(array)

if __name__ == '__main__':
	ite()

	ite2()

	ite3()

	ite4()

	ite5()

	ite6()

	ite7()
