from Ind import *

class Bary:

	def __init__(self,dimension):
		self.dimension=dimension
		self.length=0
		self.values=[]
		for i in range(dimension):
			self.values.append(0)

	def add(self,ind):
		for i in range(self.dimension):
			self.values[i]=(self.length*self.values[i]+ind.values[i])/(self.length+1)
		self.length+=1
