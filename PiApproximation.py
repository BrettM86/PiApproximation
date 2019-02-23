#Bretton May
#10/03/18
#Pi Approximation

from __future__ import division
import random

class Pie:

	@property
	def X(self):
		return self._X
	@X.setter
	def X(self, value):
		self._X = value

	@property
	def Y(self):
		return self.Y
	@Y.setter
	def X(self, value):
		self._X = value
	
	def isWithin(self, x, y):
		if x**2 + y **2 <= 1:
			return True
		else:
			return False
#------------------------------MAIN------------------------------------------
pie = Pie()
inside =  0
n = 100000
for x in range(1,n):
	pie.X = random.random()
	pie.Y = random.random()
	if pie.isWithin(pie.X, pie.Y):
		inside += 1
pie = 4*(inside / n)
percenterror = (100*(abs(pie - 3.14159265359))/3.14159265359)
print("Closest approximation to pie: {}".format(pie))
print("With an error of {:.4f}% where n = {}".format(float(percenterror) , n))