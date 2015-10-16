from Ind import *

class Bary:

	def __init__(self,dimension):
		self.dimension=dimension
		self.pop=[]
		self.values=[]
		for i in range(self.dimension):
			self.values.append(0.)

	def add(self,ind):
		self.pop.append(ind)


	def updates(self):
		for i in range(self.dimension):
			for j in range(len(self.pop)):
				self.values[i]+=float(self.pop[j].values[i])/len(self.pop)