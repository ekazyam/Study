import random as r

class Dice:
	min_num = 1
	max_num = 6
	face = max_num
	def __init__(self,min_num_op = 1,max_num_op = 6):
		self.min_num = min_num_op
		self.max_num = max_num_op
		print('OK')

	def start(self):
		return r.randint(self.min_num,self.max_num)

dice  = Dice()
print(dice.face)
print(dice.start())
