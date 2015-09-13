try:
	10/0
except:
	print('error')

try:
	10/0
	#例外を補足して変数に格納
except ZeroDivisionError as e:
	print(e)
else:
	print('例外無しで終了しました。')
finally:
	print('後処理です')

try:
	10/2
	#例外を補足して変数に格納
except ZeroDivisionError as e:
	print(e)
else:
	print('例外無しで終了しました。')
finally:
	# finallyは例外があっても無くてもどちらの処理ルートでも処理される
	print('後処理です')
