# coding:utf-8

class MyClass:
	test = 0
	def __init__(self , data):
		self.test = data

	def myprint(self):
		print ( self.test )

a = MyClass(1)
a.myprint()

b = MyClass(2)
b.myprint()

c = MyClass(3)
c.myprint()


