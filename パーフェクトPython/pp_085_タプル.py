x = (1,2,3,4)
print (x)
try:
	x[0] = 5
except:
	print('タプルは値の変更を許容しません')
	print('それ以外の挙動はlist型と同じっぽいです')
	print('変更が不可という制約があるので、listに比較すると速度が早いっぽいです')
else:
	pass
finally:
	pass