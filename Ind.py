from math import *
import random

class Ind:

	def set_values(self, values):
		self.values=values

	def __init__(self,length):
		self.values=[]
		self.length=length
		for i in range(length):
			self.values.append(random.random())


	def __eq__(self, ind):
		if ind is None:
			return False
		if not isinstance(ind, Ind):
			return False
		if not self.length == ind.length:
			return False
		for i in range(self.length):
			if not self.values[i]==ind.values[i]:
				return False
		return True

	def dist(self,ind):
		somme=0
		for i in range(self.length):
			somme+=(self.values[i]-ind.values[i])**2
		return sqrt(somme)

	def copy(self):
		i=Ind(self.length)
		i.set_values(self.values)
		return i


